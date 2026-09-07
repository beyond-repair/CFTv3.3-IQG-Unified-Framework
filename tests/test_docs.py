"""Docs-presence tests for the CFT/IQG consistency ledger.

Green tests do not validate physics. They lock required files and claim caps.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "RESEARCH.md",
    "CONSISTENCY.md",
    "GOVERNANCE.md",
    "LICENSE",
    "CFTv3.3-IQG-Unified-Framework.md",
    "CFTv3.3-IQG-Unified-Framework.tex",
]


def test_required_files_exist():
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    assert missing == [], f"missing ledger files: {missing}"


def test_research_classification():
    text = (ROOT / "RESEARCH.md").read_text(encoding="utf-8")
    assert "RESEARCH" in text
    assert "Claim ≤ 2" in text or "Claim <= 2" in text or "Claim ≤ 2" in text or "claim ≤ 2" in text.lower() or "Claim ≤ 2" in text or "Allowed claims" in text


def test_readme_is_synthesis_not_thruster():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "synthesis" in text.lower() or "consistency ledger" in text.lower()
    assert "not a thruster" in text.lower() or "not the SPARC runner" in text


def test_consistency_records_bullet_fail():
    text = (ROOT / "CONSISTENCY.md").read_text(encoding="utf-8")
    assert "Bullet" in text
    assert "FAIL" in text or "Fail" in text
