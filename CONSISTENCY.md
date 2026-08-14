# Consistency & Audit Ledger — CFTv3.3-IQG-Unified-Framework

**Last audit:** 2026-08-14  
**Auditor:** Automated structural repair pass over the full associated repository cluster.

## 1. Symbol Registry (Authoritative)

See README.md §2. Only one active definition per symbol is permitted. Redefinition requires version increment + deprecation notice.

## 2. Assumption Classification

| ID | Statement | Class |
|----|-----------|-------|
| A1 | User intent is scientific consolidation | User |
| A2 | SPARC, LRG 3-757, muonic H, Bullet Cluster are the kill-gates | Empirical |
| A3 | Standard GR + QED baselines | Literature |
| A4 | Proca + fractal LDOS + screening + PIF ontology | Model |

## 3. Conflict Register

### C1 — Ware Constant Numerical Value (Critical)
- Claim set 1: \( W_\star \approx 0.08 \) (Math.md, most READMEs, galactic/muonic formulae)
- Claim set 2: W(3) = 0.1267 (M2 table, physics_evaluator_snippet.py assert)
- Claim set 3: ghost-free requires W(n) < 0.125
- Status: Unresolved. All downstream numerical predictions that mix the two values are currently invalid.

### C2 — Lensing Amplification (High)
- phenomenology.md: ~2.2× for LRG 3-757
- Earlier target/CFT-v3.1 language: ~2.8×
- Status: Prefer 2.2× pending independent re-calculation.

### C3 — Bullet Cluster Ratio Language (Medium)
- Mixed statements of ~3× and 7–9×
- Status: Open; depends on exact partial-screening parameters (S ≈ 0.55, N_los).

### C4 — Missing Executable Artifacts (High)
Referenced but absent from public trees:
- complete physics_evaluator.py
- sierpinski_generator.py
- test_baseline_v1.py / symmetry_decomposition.py
- any SPARC fitting or lensing integration notebook

### C5 — Derivation Status (Medium)
Math.md: “W_★ is an empirical anchor; derivation is open.”  
-ware-constant-derivation README: “rigorously derived from first principles.”

## 4. Falsification Protocol (Current)

Any claim that cannot survive the following is to be demoted to Hypothesis:
1. Single consistent numerical value of W used throughout.
2. Reproducible SPARC residual and LRG θ_E calculation published with code.
3. Ghost-free dispersion relation verified for the adopted W(n).
4. Surface-integral + Poynting residual demonstrated mesh-invariant on the claimed geometry.

## 5. Recommended Immediate Actions

1. Choose and lock either W_★ = 0.08 with a revised M2 law, or adopt the tabulated values and drop the W < 0.125 bound (or raise it).
2. Publish the missing evaluation scripts or remove the “blind-build” checklists that reference them.
3. Produce a single validation notebook that computes the four kill-gates under one parameter set.

---

This ledger is the authoritative record of verified state for the synthesis layer.
