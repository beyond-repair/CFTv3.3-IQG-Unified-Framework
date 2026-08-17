# Consistency & Audit Ledger — CFTv3.3-IQG-Unified-Framework

**Last audit:** 2026-08-17 (Group 1 hygiene pass)

## 1. Symbol Registry

\(W_\star = 1/(4\pi)\approx 0.079577\) — tree-level monopole matching.  
Option A: M2 geometric only.  
Macro: \(r_0=0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}\) — verified.

## 2. Conflict Register

| ID | Topic | Status |
|----|-------|--------|
| C1 | W value | **Resolved** at matching level |
| C2 | Lensing ×2.2 | Multiplicative + δ_sat (semi-derived) |
| C3 | Bullet Cluster | Simple r0/c **FAIL**; Model D open |
| C4 | Executables | Present (see hygiene notes) |
| C5 | Bulk c_star=1 | Matching convention; bulk open |
| C6 | Local SPARC | Median χ²_red **~9.1** |

## 3. Hygiene Pass (2026-08-17)

| Action | Repo |
|--------|------|
| Quarantined `physics_evaluator_snippet.py` (raises on import) | stress-tensor-modification |
| Canonical SPARC entrypoint `sparc_run.py` → default `sparc_o1` | ware-constant-phenomenology |
| Marked CFT-v3.1 **SUPERSEDED** | CFT-v3.1 |
| Stub READMEs: pointer / hypothesis / design-goal only | coherence-drive, derivation, m2, momentum, pinch, thrust |

GitHub **short descriptions** may still lag until edited in repo Settings (CLI unavailable this pass).

## 4. Falsification Protocol

| Criterion | Result |
|-----------|--------|
| Macro r0(Mb) | **Pass** |
| Local SPARC O(1) | Open (~9) |
| Lensing ×2.2 | Pass |
| Bullet r0/c | **Fail** |
| Ghost-free Option A | Pass |

## 5. Priority Remaining Work

1. Bullet Model D (cluster ξ) from first principles  
2. Local χ² → O(1)  
3. Non-minimal bulk c_star  
4. λ_A → numerical δ_sat  
5. Optional: update GitHub UI descriptions to match READMEs  

---

Authoritative verified-state record. No speculative result is marked closed.
