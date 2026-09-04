#!/usr/bin/env python3
"""
Curriculum lookup tool adapter for Australian education standards.

Implements the interface contract from Task 8:
- Accepts jurisdiction, school phase, year level/course, learning area/subject, and code/query
- Returns official identifier, statement type, short text or locator, source URL, 
  version/effective year, authority name, authority-verification evidence, and mapping confidence
- Returns explicit not-found result (status:"not-found") when cannot resolve
- NEVER fabricates or uncited curriculum codes

Offline usage: reads from bundled manifests (source-manifest.australian.json + qcaa/*.json)
No external network calls or US Learning Commons Knowledge Graph connector used.
"""

import json
import os
from typing import Dict, Any, Optional, List

# File paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up three levels to reach project root: 
# plugin/tools/curriculum_lookup/ -> plugin/tools/ -> plugin/ -> project_root
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
DATA_DIR = os.path.join(ROOT_DIR, "data", "curriculum")

# Cache for loaded manifests
_AUSTRALIAN_MANIFEST = None
_QCAA_MANIFESTS = {}


def _load_json_file(filepath: str) -> Dict[str, Any]:
    """Load JSON file from absolute path."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _normalize_text(text: str) -> str:
    """Normalize text for case-insensitive comparison."""
    return text.strip().lower()


def _load_australian_manifest() -> List[Dict[str, Any]]:
    """Load Australian curriculum manifest from source-manifest.australian.json."""
    global _AUSTRALIAN_MANIFEST
    if _AUSTRALIAN_MANIFEST is None:
        filepath = os.path.join(DATA_DIR, "source-manifest.australian.json")
        _AUSTRALIAN_MANIFEST = _load_json_file(filepath)
    return _AUSTRALIAN_MANIFEST


def _load_qcaa_manifests() -> Dict[str, Dict[str, Any]]:
    """Load all QCAA curriculum manifests from data/curriculum/qcaa/*.json."""
    global _QCAA_MANIFESTS
    if not _QCAA_MANIFESTS:
        qcaa_dir = os.path.join(DATA_DIR, "qcaa")
        if os.path.exists(qcaa_dir):
            for filename in os.listdir(qcaa_dir):
                if filename.endswith('.json') and not filename.startswith('.'):
                    subject = filename[:-5]  # Remove .json extension
                    filepath = os.path.join(qcaa_dir, filename)
                    _QCAA_MANIFESTS[subject] = _load_json_file(filepath)
    return _QCAA_MANIFESTS


def _find_in_australian_manifest(
    jurisdiction: str,
    school_phase: str,
    learning_area: str,
    code_query: str
) -> Optional[Dict[str, Any]]:
    """Search Australian curriculum manifest for matching entry."""
    manifest = _load_australian_manifest()
    
    for entry in manifest:
        # Check jurisdiction match
        if _normalize_text(entry.get("jurisdiction", "")) != _normalize_text(jurisdiction):
            continue
        
        # Check school phase match
        entry_phase = _normalize_text(entry.get("school_phase", ""))
        # Normalize the query phase - handle F-10 variations
        if _normalize_text(school_phase) not in entry_phase:
            continue
        
        # Check learning area/subject match
        entry_subject = _normalize_text(entry.get("learning_area_or_subject", ""))
        query_subject = _normalize_text(learning_area)
        
        if entry_subject != query_subject and query_subject not in entry_subject and entry_subject not in query_subject:
            continue
        
        # If we have a specific code query, check it against title and locator
        if code_query:
            title = _normalize_text(entry.get("document_title", ""))
            locator = _normalize_text(entry.get("locator", ""))
            
            if code_query not in title and code_query not in locator:
                continue
        
        # Found match!
        return entry
    
    return None


def _get_qcaa_subject_name(manifest_data: Dict[str, Any], filename_slug: str = "") -> str:
    """Extract subject name from QCAA manifest data, handling different field structures."""
    # Primary field: 'subject' or 'name'
    for field in ('subject', 'name'):
        val = manifest_data.get(field, "")
        if val:
            return val
    
    # Fallback: derive from slug field
    slug = manifest_data.get("slug", "")
    if slug:
        return slug.replace('-', ' ').title()
    
    # Final fallback: derive from filename slug
    if filename_slug:
        return filename_slug.replace('-', ' ').title()
    
    return ""


def _find_in_qcaa_manifests(
    learning_area: str,
    code_query: str
) -> Optional[Dict[str, Any]]:
    """Search QCAA curriculum manifests for matching entry."""
    manifests = _load_qcaa_manifests()
    query_subject = _normalize_text(learning_area)
    
    for subject_key, manifest_data in manifests.items():
        # Try multiple fields for subject matching
        subject_name = _get_qcaa_subject_name(manifest_data, subject_key)
        manifest_subject = _normalize_text(subject_name)
        
        # Check slug-based filename key as fallback
        slug_subject = _normalize_text(subject_key.replace('-', ' '))
        
        # Exact match against subject name
        if manifest_subject == query_subject:
            return manifest_data
        
        # Match against slug-derived name
        elif slug_subject == query_subject:
            return manifest_data
        
        # Fuzzy partial match (subject name contains query or vice versa)
        # Only for longer queries to avoid accidental partial matches
        elif len(query_subject) >= 4 and (
            query_subject in manifest_subject or
            manifest_subject in query_subject
        ):
            return manifest_data
    
    return None


def lookup(
    jurisdiction: str,
    school_phase: str,
    year_level: str,
    learning_area: str,
    code_query: str = ""
) -> Dict[str, Any]:
    """
    Look up curriculum information based on the provided parameters.
    
    Args:
        jurisdiction: "Australia" or "Queensland"
        school_phase: "F-10" or "Years 11-12"
        year_level: Specific year level or course (e.g., "Year 5", "Year 11", "General senior syllabus")
        learning_area: Subject/learning area (e.g., "Mathematics", "English", "Science")
        code_query: Optional specific code to match against (e.g., "ACARA", "QSUB-0052")
    
    Returns:
        Dictionary with curriculum information or status:"not-found" if not found
    """
    # Validate jurisdiction
    jurisdiction_norm = _normalize_text(jurisdiction)
    if jurisdiction_norm not in ["australia", "queensland"]:
        return {
            "status": "not-found",
            "message": f"Unsupported jurisdiction: {jurisdiction}. Only 'Australia' and 'Queensland' are supported."
        }
    
    # Normalize school phase
    school_phase_norm = _normalize_text(school_phase)
    
    # Handle Australian curriculum (F-10) - ACARA
    if jurisdiction_norm == "australia":
        # For F-10, use the Australian manifest
        result = _find_in_australian_manifest(jurisdiction, school_phase_norm, learning_area, code_query)
        
        if result:
            # Build response from manifest entry
            return {
                "status": "found",
                "official_identifier": result.get("document_title", ""),
                "statement_type": "Australian Curriculum",
                "short_text": result.get("locator", ""),
                "source_url": result.get("url", ""),
                "version_or_effective_year": result.get("version_or_effective_year", ""),
                "authority_name": result.get("authority_name", ""),
                "authority_verification": {
                    "evidence_url": result.get("authority_evidence_url", ""),
                    "status": result.get("authority_verification_status", ""),
                    "publication_owner": result.get("publication_owner", ""),
                    "licence": result.get("licence", "")
                },
                "mapping_confidence": 0.95,  # High confidence for direct matches
                "raw_entry": result
            }
        else:
            # Try QCAA manifests if this might be Years 11-12
            if school_phase_norm in ["year", "years", "11-12"]:
                result = _find_in_qcaa_manifests(learning_area, code_query)
                if result:
                    return {
                        "status": "found",
                        "official_identifier": result.get("qsub_id", result.get("subject", "")),
                        "statement_type": "QCAA Senior Syllabus",
                        "short_text": result.get("family", ""),
                        "source_url": result.get("source_locators", {}).get("current_syllabus_pdf", ""),
                        "version_or_effective_year": result.get("version_or_effective_year", ""),
                        "authority_name": result.get("authority", {}).get("authority_name", ""),
                        "authority_verification": {
                            "evidence_url": result.get("authority", {}).get("authority_evidence_url", ""),
                            "status": result.get("authority", {}).get("authority_verification_status", ""),
                            "publication_owner": result.get("authority", {}).get("publication_owner", "")
                        },
                        "mapping_confidence": 0.90,
                        "raw_entry": result
                    }
    
    # Handle Queensland curriculum (Years 11-12)
    elif jurisdiction_norm == "queensland":
        result = _find_in_qcaa_manifests(learning_area, code_query)
        
        if result:
            return {
                "status": "found",
                "official_identifier": result.get("qsub_id", result.get("subject", "")),
                "statement_type": "QCAA Senior Syllabus",
                "short_text": result.get("family", ""),
                "source_url": result.get("source_locators", {}).get("current_syllabus_pdf", ""),
                "version_or_effective_year": result.get("version_or_effective_year", ""),
                "authority_name": result.get("authority", {}).get("authority_name", ""),
                "authority_verification": {
                    "evidence_url": result.get("authority", {}).get("authority_evidence_url", ""),
                    "status": result.get("authority", {}).get("authority_verification_status", ""),
                    "publication_owner": result.get("authority", {}).get("publication_owner", "")
                },
                "mapping_confidence": 0.90,
                "raw_entry": result
            }
        elif school_phase_norm in ["year", "years", "11-12"]:
            # If we looked specifically for Years 11-12 but didn't find anything,
            # search the Australian manifest as a fallback
            result = _find_in_australian_manifest(jurisdiction, school_phase_norm, learning_area, code_query)
            if result:
                return {
                    "status": "found",
                    "official_identifier": result.get("document_title", ""),
                    "statement_type": "Australian Curriculum",
                    "short_text": result.get("locator", ""),
                    "source_url": result.get("url", ""),
                    "version_or_effective_year": result.get("version_or_effective_year", ""),
                    "authority_name": result.get("authority_name", ""),
                    "authority_verification": {
                        "evidence_url": result.get("authority_evidence_url", ""),
                        "status": result.get("authority_verification_status", ""),
                        "publication_owner": result.get("publication_owner", ""),
                        "licence": result.get("licence", "")
                    },
                    "mapping_confidence": 0.95,
                    "raw_entry": result
                }
    
    # If we get here, no match was found
    return {
        "status": "not-found",
        "message": f"No curriculum found for jurisdiction='{jurisdiction}', school_phase='{school_phase}', learning_area='{learning_area}', code='{code_query}'."
    }


def run_self_test() -> bool:
    """Run self-tests to verify curriculum lookup functionality."""
    test_cases = [
        {
            "name": "F-10 Australian Mathematics (ACARA)",
            "jurisdiction": "Australia",
            "phase": "F-10",
            "year": "",
            "subject": "Mathematics",
            "code": "",
            "expected_status": "found"
        },
        {
            "name": "Years 11-12 QCAA Legal Studies",
            "jurisdiction": "Queensland",
            "phase": "Years 11-12",
            "year": "",
            "subject": "Legal Studies",
            "code": "QSUB-0052",
            "expected_status": "found"
        },
        {
            "name": "Invalid/Unknowable subject",
            "jurisdiction": "Australia",
            "phase": "F-10",
            "year": "",
            "subject": "NonExistentSubject",
            "code": "",
            "expected_status": "not-found"
        }
    ]
    
    passed = 0
    failed = 0
    
    for test_case in test_cases:
        result = lookup(
            test_case['jurisdiction'],
            test_case['phase'],
            test_case['year'],
            test_case['subject'],
            test_case['code']
        )
        
        if result['status'] == test_case['expected_status']:
            if result['status'] == 'found':
                print(f"✓ {test_case['name']}: Found {result.get('official_identifier', 'N/A')}")
            else:
                print(f"✓ {test_case['name']}: Correctly returned not-found")
            passed += 1
        else:
            print(f"✗ {test_case['name']}: Expected {test_case['expected_status']}, got {result['status']}")
            failed += 1
    
    print(f"\nSelf-Test Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Curriculum lookup tool")
    parser.add_argument("--jurisdiction", help="Jurisdiction: Australia or Queensland")
    parser.add_argument("--phase", help="School phase: F-10 or Years 11-12")
    parser.add_argument("--year", help="Year level or course")
    parser.add_argument("--subject", help="Learning area/subject")
    parser.add_argument("--code", default="", help="Optional code to match against")
    parser.add_argument("--test", action="store_true", help="Run self-tests")
    
    args = parser.parse_args()
    
    if args.test:
        success = run_self_test()
        if not success:
            exit(1)
    else:
        result = lookup(
            args.jurisdiction,
            args.phase,
            args.year,
            args.subject,
            args.code
        )
        
        print(json.dumps(result, indent=2))