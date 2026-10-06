"""Symbol-lock tests for the CFT/IQG consistency ledger.

These checks lock registered strings. They do not derive W, recompute SPARC,
or validate the modified Einstein equation.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FROZEN = "0.23(n-3)"
DEPRECATED = "0.23(n-1)"


def _read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_frozen_weight_is_n_minus_3():
    readme = _read("README.md")
    consistency = _read("CONSISTENCY.md")
    assert FROZEN in readme
    assert FROZEN in consistency
    assert "Deprecated for new work" in readme
    assert "Deprecated for new work" in consistency
    assert DEPRECATED in readme
    assert DEPRECATED in consistency


def test_phenomenology_anchor_registered():
    readme = _read("README.md")
    consistency = _read("CONSISTENCY.md")
    anchor = "0.079577"
    pi_token = "4" + chr(92) + "pi"
    assert anchor in readme
    assert pi_token in consistency or pi_token in readme


def test_bullet_cluster_remains_fail():
    text = _read("CONSISTENCY.md")
    assert "Bullet" in text
    assert "FAIL" in text


def test_claim_cap_not_elevated():
    research = _read("RESEARCH.md")
    gov = _read("GOVERNANCE.md")
    assert "RESEARCH" in research
    assert "RESEARCH" in gov
    assert "Experimental confirmation" in research
    assert "not a thruster" in _read("README.md").lower()


def test_no_physics_executable_claimed_in_tree():
    research = _read("RESEARCH.md")
    assert "none in this tree" in research
