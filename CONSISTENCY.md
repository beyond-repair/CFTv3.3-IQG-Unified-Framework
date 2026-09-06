# Consistency & Audit Ledger — CFTv3.3-IQG-Unified-Framework

**Last audit:** 2026-09-06 (Sweep-082 — live tree + CI absence re-verified; no new physics claims)

## 1. Symbol Registry

$W_\star = 1/(4\pi)\approx 0.079577$ — tree-level monopole matching.  
Option A: M2 geometric only.  
Macro: $r_0=0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}$ — verified at the matching-convention level recorded in prior hygiene notes (not re-computed this sweep).

Canonical recursive weight (frozen for residual-force work):

$$W(n) = 0.08\, e^{0.23(n-3)}$$

Deprecated for new work: $W(n)=0.08\,e^{0.23(n-1)}$.

## 2. Conflict Register

| ID | Topic | Status |
|----|-------|--------|
| C1 | W value | **Resolved** at matching level |
| C2 | Lensing ×2.2 | Multiplicative + δ_sat (semi-derived) |
| C3 | Bullet Cluster | Simple r0/c **FAIL**; Model D open |
| C4 | Executables | Live in satellite repos, not this tree |
| C5 | Bulk c_star=1 | Matching convention; bulk open |
| C6 | Local SPARC | Median χ²_red **~9.1** (not O(1)) |

## 3. Hygiene Pass + Sweep-082 note

This tree contains only markdown/TeX/LICENSE. No tests, no CI — acceptable for a ledger repo. Physics executables must remain in satellite repos.

Sweep-082 Actions API: workflows total_count=0. Releases=[]. Tags=[].

## 4. Falsification Protocol

| Criterion | Result |
|-----------|--------|
| Macro r0(Mb) | **Pass** (prior record; not re-run Sweep-082) |
| Local SPARC O(1) | Open (~9) |
| Lensing ×2.2 | Pass (prior record) |
| Bullet r0/c | **Fail** |
| Ghost-free Option A | Pass (prior record) |

## 5. Priority Remaining Work

1. Bullet Model D (cluster ξ) from first principles  
2. Local χ² → O(1)  
3. Non-minimal bulk c_star  
4. λ_A → numerical δ_sat  
5. Optional: update GitHub UI descriptions to match READMEs  

---

Authoritative verified-state record. No speculative result is marked closed.
