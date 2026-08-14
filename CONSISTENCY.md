# Consistency & Audit Ledger — CFTv3.3-IQG-Unified-Framework

**Last audit:** 2026-08-14 (local tuning / full-wave / spectral pass)

## 1. Symbol Registry

Option A locked: \(W_\star=0.08\) sole gravitational coupling. M2 = geometric enhancement only.

## 2. Conflict Register

### C1 — Ware Constant Value
**RESOLVED (Option A).**

### C2 — Lensing Amplification
**ADVANCED; target not recovered.** Soft saturation + geometric_prefactor≈0.16 + multi-plane integrator yields amplification factor O(0.1) at cosmological Einstein radii, not the phenomenological target ~2.2. Soft |A|^4 saturation suppresses Ware deflection when \(b\sim R_E\gg r_\mathrm{sat}\). Recovering ~2.2 requires slower saturation or a different coupling into the lens potential.

### C3 — Bullet Cluster
Open.

### C4 — Executable Artifacts
**RESOLVED** for current scope, including full-wave EFIE BEM (`fullwave_bem.py`).

### C5 — First-Principles \(W_\star\)
**Open.** Finite-mesh spectral ratios do not yield 0.08. Closest analytic coincidence remains \(1/(4\pi)\approx0.0796\). Toy one-loop model is parameter-sensitive. Continuum spectral or derived effective-potential calculation still required.

### C6 — SPARC Fit Quality
**RE-FRAMED + PARTIALLY IMPROVED.**
- Macro \(r_0(M_b)\): **VERIFIED**.
- Local χ² (untuned): median ~35–40.
- Local χ² (Υ + β tuned, macro frozen): median ~14; 22% of galaxies < 5; 41% < 10. Progress, not closure.

## 3. Falsification Protocol Status

| Criterion | Status |
|-----------|--------|
| Single consistent W in gravity | Pass |
| Macro \(r_0(M_b)\) scaling | **Pass** |
| Local SPARC \(\chi^2\sim\mathcal{O}(1)\) | Improved (~14); not yet O(1) |
| Lensing factor ~2.2 under soft sat | **Not recovered** |
| Ghost-free under Option A | Pass |
| Full-wave surface residual | EFIE BEM present (piecewise-constant / PEC) |

## 4. Priority Remaining Work

1. Further local profile structure (or limited galaxy-to-galaxy coupling variation) to push median χ²_red toward O(1).
2. Lensing: slower saturation or alternative W-coupling to recover O(1) amplification at cosmological scales.
3. Continuum spectral / derived effective-potential derivation of \(W_\star\).
4. Higher-order (RWG) full-wave BEM if engineering precision is required.

---

Authoritative verified-state record for the synthesis layer.
