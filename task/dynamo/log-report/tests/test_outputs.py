import json
from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_valid_json():
    """The report file contains valid JSON."""
    try:
        with open("/app/report.json") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise AssertionError(f"report.json is not valid JSON: {e}")


def test_report_has_required_fields():
    """The report contains all required fields."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    required_fields = {"total_requests", "unique_ips", "top_path"}
    assert required_fields.issubset(data.keys()), f"Missing fields. Expected {required_fields}, got {set(data.keys())}"


def test_report_values_correct():
    """The report values match the access log."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    # Count actual values from the log
    ips = set()
    total = 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
    
    assert data["total_requests"] == total, f"total_requests mismatch: got {data['total_requests']}, expected {total}"
    assert data["unique_ips"] == len(ips), f"unique_ips mismatch: got {data['unique_ips']}, expected {len(ips)}"
    assert isinstance(data["top_path"], str) and len(data["top_path"]) > 0, "top_path must be a non-empty string"
