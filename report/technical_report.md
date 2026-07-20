# Symbolic Investigation of the Proposed Three-Dimensional Jacobian Counterexample

**Exact elimination, fiber classification, and analysis of the third-variable channel**

**Date:** 20 July 2026  
**Arithmetic:** Exact rational and algebraic arithmetic throughout  
**Primary CAS:** SymPy 1.14.0  
**Independent check:** Nerdamer 1.1.13

## Executive conclusion

The displayed map passes the two elementary counterexample checks exactly: its Jacobian determinant is the constant −2, and the three reported points have the common image (−1/4,0,0). The special-fiber ideal has the proposed reduced Gröbner basis.

The reported collision is not isolated and is not confined to an exceptional target locus. It is the a=−1/4 member of the exact one-parameter family

    F⁻¹(a,0,0) = {(0,0,a), (r,6ar,−26a) : 4ar²+1=0},   a ≠ 0.

More strongly, elimination exposes a three-sheeted generic finite map. Define

    Q = 27a²c² − 18abc + 16a + b³c − b²,
    R = 4 − 3bc,
    L = 27ac² − 9bc + 8.

The elimination ideal in Q[a,b,c,x] is generated, up to a nonzero rational scalar, by

    P(x) = Qx³ + Rx − 2c.

Its discriminant and an associated identity are

    Discₓ(P) = −4 L² Q,
    R³ + 27Qc² = L².

On the Zariski-open set QL ≠ 0, P has three distinct x-roots and each root lifts uniquely to a solution of the full three-equation system. Thus the generic fiber contains exactly three reduced points over C. The known target has Q=−4 and L=8, so it lies in this open three-sheeted region.

The true fiber-cardinality drop occurs on Q=0: away from R=0 the fiber has one point; when Q=R=0 the fiber is empty. The image complement is the curve

    (a,b,c) = (4/(27c²), 4/(3c), c),   c ≠ 0.

The locus L=0 is subtler: the x-eliminant has a repeated root, but the full fiber still has three distinct reduced points. Two points share the same x-coordinate and separate in y and z. Accordingly, L=0 is a discriminant locus for the projection of a fiber to x, not a ramification locus of F.

The third variable is structurally essential within the tested ansätze. It is best described as both an auxiliary compatibility variable and a determinant-balancing channel. It is not the generic branch label: the three generic branches are labeled by the three x-roots. No genuinely distinct parameter family was found in the restricted coefficient search; all surviving parameters are diagonal rescalings of the original map.

## 1. Scope, reliability, and status language

The investigation was designed to distinguish four kinds of statements.

- **Verified result:** established by exact symbolic identities, exact Gröbner bases, or exact substitution into the original system.
- **Computational observation:** exact within the stated CAS computation or coefficient ansatz, but not promoted beyond that scope.
- **Conjectural interpretation:** explanatory language such as “determinant compensator” or claims about what dimension three makes possible.
- **Not attempted or infeasible here:** exhaustive classification of all nearby maps, a formal proof-assistant verification, and a proof of any two-dimensional impossibility theorem.

No generic fiber claim below is inferred merely from the degree of P. Roots are linked back to the full ideal. All loci introduced by division in convenient reconstruction formulas are analyzed separately. No numerical root finder is used as evidence.

## 2. Phase 1 — independent verification

Let u=1+xy. The map is

    F₁ = u³z + y²u(4+3xy),
    F₂ = y + 3xu²z + 3xy²(4+3xy),
    F₃ = 2x − 3x²y − x³z.

### 2.1 Constant Jacobian

SymPy gives, after exact differentiation, determinant formation, expansion, and factorization,

    det(JF) = −2.

Nerdamer independently returns the same exact constant. Both checks are assertion-backed in the supplied source.

### 2.2 Reported three-point collision

Both systems return

    F(0,0,−1/4) = (−1/4,0,0),
    F(1,−3/2,13/2) = (−1/4,0,0),
    F(−1,3/2,13/2) = (−1/4,0,0).

These are exact rational evaluations.

### 2.3 Reduced Gröbner basis of the reported fiber

For the ideal

    I₀ = ⟨F₁+1/4, F₂, F₃⟩ ⊂ Q[x,y,z],

the reduced lexicographic basis with variable order z>y>x is

    z − 27x²/4 + 1/4,
    y + 3x/2,
    x³ − x.

Equivalently, after harmless nonzero scalar multiplication,

    x(x−1)(x+1)=0,
    2y+3x=0,
    4z+1−27x²=0.

Each proposed generator has zero remainder modulo the computed reduced basis, and conversely the displayed systems differ only by nonzero scalar normalization. The fiber therefore consists exactly of the three reported reduced points.

## 3. Phase 2 — generic elimination and full-fiber classification

### 3.1 Denominator-free elimination

The generic ideal is

    I = ⟨F₁−a, F₂−b, F₃−c⟩ ⊂ Q[a,b,c,x,y,z].

A reduced lexicographic Gröbner basis computed over the polynomial ring—not over a rational-function field—contains exactly one polynomial free of y and z. Its primitive normalization is

    P(x) = (27a²c²−18abc+16a+b³c−b²)x³ +(4−3bc)x−2c.

Consequently,

    I ∩ Q[a,b,c,x] = ⟨P(x)⟩.

This construction introduces no denominator-clearing factors. Direct substitution also verifies the polynomial identity

    P(F₁,F₂,F₃;x) ≡ 0

in Q[x,y,z].

### 3.2 Generic degree and validation against the full system

When QL≠0, the Gröbner basis over Q(a,b,c) has triangular form

    P(x)=0,
    y = Y(a,b,c,x),
    z = Z(a,b,c,x),

where the reconstruction denominators divide powers of Q and L. The cubic has three distinct roots because Discₓ(P)=−4L²Q is nonzero. The triangular equations give one and only one y,z pair for each x-root. Substitution/reduction against the original three equations is exact.

As a non-rational sample, the target (2,1,1) produces

    104x³+x−2=0,
    y = (−5304x²+624x+19)/106,
    z = (4680x²+96720x−29491)/424.

Reducing all three original residuals modulo 104x³+x−2 gives zero. Thus all three algebraic roots—not only a selected numerical root—lift to the full fiber.

This establishes generic geometric degree three. Conceptually, after localization at the target function field, the source coordinate ring remains a domain; the triangular presentation makes it a finite degree-three algebra generated by x. The generic fiber is therefore not an artifact of a reducible or spurious eliminant.

### 3.3 The exact family containing the posted fiber

For every a≠0,

    P(x)|_(b=c=0) = 4x(4ax²+1).

The complete fiber is

    (0,0,a),
    (r,6ar,−26a), where r is either root of 4ar²+1=0.

For a=−1/4, the two nonzero roots are r=±1 and the formulas reproduce the posted points. Other exact rational examples include

    F⁻¹(−1,0,0) = {(0,0,−1), (1/2,−3,26), (−1/2,3,26)},
    F⁻¹(−1/9,0,0) = {(0,0,−1/9), (3/2,−1,26/9), (−3/2,1,26/9)},
    F⁻¹(−4,0,0) = {(0,0,−4), (1/4,−6,104), (−1/4,6,104)}.

For a=1 the extra points are complex but still exact:

    (i/2,3i,−26), (−i/2,−3i,−26).

As a→0 along this family, the two noncentral preimages satisfy |x|→∞ while y,z→0; the finite preimage (0,0,a) tends to (0,0,0). This explicitly exhibits the loss of two sheets at infinity without any finite critical point.

### 3.4 Exceptional loci and fiber counts

The identities

    Discₓ(P)=−4L²Q,
    L²=R³+27Qc²

make the case split exact.

| Output condition | x-eliminant behavior | Full fiber over C |
|---|---|---|
| Q≠0, L≠0 | cubic, three distinct x-roots | 3 distinct reduced points |
| Q≠0, L=0 | cubic with one double x-root | 3 distinct reduced points; two share x |
| Q=0, R≠0 | linear | 1 reduced point |
| Q=0, R=0 | nonzero constant −2c | empty |

In the last row, R=0 implies bc=4/3 and c≠0. Imposing Q=0 then gives

    a=4/(27c²), b=4/(3c), c≠0.

At the exact sample (4/27,4/3,1), the specialized reduced Gröbner basis is {1}.

On Q=0,R≠0, L cannot vanish because L²=R³. The eliminant has the single root x=2c/R, and the remaining triangular equations lift it uniquely. At the exact sample (0,0,2), the basis is {z,y,x−1}.

### 3.5 Why L=0 does not mean a multiple full-fiber point

Take the exact target (−8/27,0,1), for which L=0 and Q=−64/27. The reduced basis yields the three exact points

    (−3/2, 4/3, 104/27),
    (3/4, 2(−1+√3)/3, −8(−13+9√3)/27),
    (3/4, −2(1+√3)/3, 8(13+9√3)/27).

The latter two share x=3/4. They are nevertheless distinct solutions, and direct substitution returns the target exactly.

More generally, on L=0,Q≠0 write d=3bc−4. Then c≠0 and d≠0. The two x-values are

    x=6c/d,
    x=−3c/d.

The second is the double root of P but supports two y-values

    y=(d+2±√(−3d))/(3c),

which are distinct because d≠0. The Jacobian determinant −2 ensures that every full solution is simple. The repeated factor belongs only to the projection of the fiber onto x.

### 3.6 Positive-dimensional fibers, multiplicities, image, and nonproperness

There are no positive-dimensional fibers. At every source point the three differentials dF₁,dF₂,dF₃ are linearly independent, so the local fiber dimension is zero. Equivalently, the morphism is étale and hence quasi-finite.

All finite fiber points are reduced: the Jacobian matrix of the three fiber equations is nonsingular at every solution. Therefore the drops from three points to one or zero on Q=0 are not hidden multiplicity transfers.

The exact image is

    C³ minus {(4/(27c²),4/(3c),c):c≠0}.

Using the standard fiber-count characterization for a generically finite polynomial map, the nonproperness set is exactly the hypersurface Q=0: those and only those targets have fewer than the generic three reduced preimages. This is the algebraic location where sheets escape to infinity.

## 4. Phase 3 — role of the third variable

Write F=A+zB, with

    A = (y²u(4+3xy), y+3xy²(4+3xy), 2x−3x²y),
    B = (u³, 3xu², −x³).

### 4.1 Exact determinant cancellation

With subscripts denoting partial derivatives,

    det JF = det(Aₓ+zBₓ, Aᵧ+zBᵧ, B).

The four exact scalar triple products are

    det(Aₓ,Aᵧ,B) = −2,
    det(Bₓ,Aᵧ,B) = −6x²u,
    det(Aₓ,Bᵧ,B) = +6x²u,
    det(Bₓ,Bᵧ,B) = 0.

Hence the coefficient of z cancels term-for-term and the coefficient of z² vanishes, leaving −2. The final identity is also reflected in

    B₂³ + 27B₁²B₃ = 0,

which places B on a cubic cone and makes its radial direction dependent on the tangent directions.

This gives exact content to “determinant compensator”: the z-channel is tuned so its nonconstant determinant contributions cancel while its ∂/∂z column supplies the nonzero constant volume form.

### 4.2 Elimination of z without division

For target T=(a,b,c), a z exists with T=A+zB exactly when

    (T−A)×B=0.

The three 2×2 minors are a division-free elimination system. Although individual minors factor by u² or x, those factors must not be divided out globally. The vector B is never zero: if x=0 then B₁=1; if u=0 then x≠0 and B₃=−x³≠0. Thus the open sets u≠0 and x≠0 cover the domain and z is uniquely recovered on at least one chart. This avoids losing the x=0 branch or the u=0 branch.

Solving F₃ for z by dividing by x³ would lose the central point (0,0,a) in the exact family above. The polynomial-ring Gröbner elimination and cross-product formulation do not make that division.

### 4.3 Algebraic role classification

- **Auxiliary compatibility variable — yes.** For fixed x,y, z moves the output along the affine line A(x,y)+zB(x,y). Eliminating it imposes compatibility between the target and that line.
- **Determinant compensator — yes, within a precise structural meaning.** Its derivatives generate equal-and-opposite z-linear triple products, and the z² term vanishes.
- **Branch-label variable — not generically.** On QL≠0, the branch choice is the root of P(x); y and z are then unique functions of that root and the target. On L=0, z helps distinguish the two points sharing x, but it is still constrained rather than freely labeling a sheet.

### 4.4 Comparison with two variables

A two-variable map has no third Jacobian column B and no affine-line compatibility variable to absorb the target while the two tangent corrections cancel. Therefore this exact A+zB mechanism has no literal two-variable copy.

That statement is not a proof that every analogous two-variable strategy is impossible. A planar map might encode compensation through a different algebraic structure, and the plane Jacobian conjecture is not addressed here. The calculation establishes a concrete three-coordinate mechanism, not a general dimension obstruction.

## 5. Phase 4 — restricted exact family search

### 5.1 Independent scaling of the three z-components

Replace B by

    (pB₁,qB₂,rB₃).

Solving every nonconstant coefficient of det JF=constant gives

    p=r,
    q=r,

with constant determinant −2p. Thus p=q=r≠0 is necessary and sufficient in this restricted test. It is merely the domain rescaling z↦pz; it does not produce a genuinely distinct family.

### 5.2 Six-coefficient structural ansatz

The broader ansatz was

    u=h+xy,
    G₁=u³z+y²u(m+nxy),
    G₂=y+pxu²z+pxy²(m+nxy),
    G₃=sx−px²y+kx³z.

The constant term of det JG is −h³s. On the nonzero-determinant component h s≠0, the exact coefficient constraints reduce to

    k=−s²/4,
    m=8/s,
    n=6/(hs),
    p=3s/(2h).

Two parameters remain, but every resulting map is diagonally equivalent to the original F:

    G_{h,s} = diag(2h³/s,h,s/2) ∘ F ∘ diag(1,1/h,s/2).

Noninjectivity therefore persists, but only because invertible affine rescalings preserve it. The three colliding source points and target can be transported explicitly through these diagonal maps.

### 5.3 Family-search conclusion

No genuinely distinct map was found within either restricted ansatz. The surviving degrees of freedom are affine rescalings. This is not an exhaustive deformation calculation: coefficients outside the displayed structural pattern were not parameterized, and no numerical candidates are reported.

## 6. Literature and provenance note

The displayed formula was posted publicly by Levent Alpöge on 20 July 2026, crediting Akhil Mathew for posing the question and Claude Fable for working on it. At the time of this report, no archival paper or author-supplied derivation was located, and the exact formula did not appear in the pre-2026 literature searches performed here.

Several established bodies of work closely frame the computation:

- Bass, Connell, and Wright’s degree-reduction theorem shows that the general Jacobian conjecture can be reduced to cubic homogeneous maps after increasing dimension. It does not predict this fixed three-dimensional degree-(7,6,4) example, but it explains why coefficient searches and normal forms are central.
- Jelonek’s theory of the nonproperness set of a dominant generically finite polynomial map gives the natural interpretation of Q=0. For an étale map, a fiber-count drop is a failure of properness rather than finite ramification. The explicit family a→0 displays that phenomenon directly.
- Kulikov morphisms are degree-three noninjective étale morphisms from certain exotic smooth affine surfaces to the plane and are counterexamples to a generalized Jacobian conjecture. They are a genuine resemblance in geometric degree and “sheets lost at infinity,” but their source is not affine space. The present formula, if retained after community verification, crosses precisely that boundary.
- Pinchuk-type maps are noninjective polynomial local diffeomorphisms of R² for the strong real Jacobian conjecture, but their Jacobian is nowhere zero rather than a nonzero constant and their complexifications do not provide the same complex Keller-map phenomenon.
- Recent historical work on the conjecture emphasizes that control at infinity is the recurrent failure point in proposed proofs. Here the obstruction is explicit: Q=0 is where two of three sheets escape to infinity.

The literature search found no earlier identical A+zB formula and no theorem naming this particular cubic eliminant. Because the result was hours old during the search, that negative finding should be treated as provisional.

## 7. Verified results, observations, interpretations, and limitations

### Verified exact results

- det JF=−2 in two independent symbolic systems.
- The three posted points share the stated image.
- The proposed special-fiber Gröbner basis is correct.
- The generic x-elimination ideal is generated by P=Qx³+Rx−2c.
- Discₓ(P)=−4L²Q and L²=R³+27Qc².
- The generic fiber has three reduced points, validated against the full system.
- The posted collision belongs to the exact a-family of three-point fibers.
- Q=0 is the fiber-cardinality drop locus; Q=R=0 is the missing-image curve.
- L=0 does not reduce the number of full points.
- No positive-dimensional or nonreduced fibers occur.
- The exact z-channel determinant cancellations have the four triple-product values listed above.
- The restricted coefficient constraints and diagonal-equivalence formulas are exact.

### Computational observations limited to stated calculations

- The x-coordinate is a primitive generic branch coordinate off the reconstruction loci.
- The hypersurface Q=0 is exactly the nonproperness set, using the verified fiber counts and the standard properness/fiber-count theorem.
- The L=0 phenomenon is best viewed as a bad projection coordinate, not a singular fiber.

### Conjectural or interpretive statements

- “Determinant compensator” is an explanatory label for the verified triple-product cancellation, not a standard theorem name.
- The example suggests that an extra coordinate can support determinant-preserving global folding through escape at infinity. It does not prove a universal qualitative divide between dimensions two and three.
- No claim is made that the restricted rescaling family exhausts meaningful deformations of the map.

### Failed, infeasible, or deliberately unattempted work

- A second CAS was available for determinant and point evaluation, but not for a fully independent generic Gröbner-basis computation in this environment. The generic result was instead cross-validated by polynomial-ring elimination, direct identities, specialization, and exact substitution.
- No Lean, Isabelle, Coq, Magma, Maple, Mathematica, SageMath, or Singular verification was performed.
- No exhaustive coefficient-space search was attempted.
- No proof concerning the two-dimensional Jacobian conjecture was attempted.
- No claim of priority or prior-literature absence should be made until an archival version and expert literature review appear.

## 8. Concise answers to the requested questions

**Does elimination expose a genuine multibranch mechanism?** Yes. The generic eliminant is a cubic, and all three roots lift to the full system on a dense open set. The mechanism is not a denominator artifact.

**Is the known fiber generic or exceptional?** It is representative of the generic three-point fiber. Its target satisfies Q≠0 and L≠0, and it belongs to an explicit one-parameter family of three-point fibers.

**Is the third coordinate structurally essential?** It is essential to the displayed construction and to the tested coefficient ansätze. It supplies both the compatibility direction and the tuned determinant cancellation. This does not prove that every possible counterexample requires an analogous variable.

**Was a nontrivial parameter family found?** A family of multibranch targets for the fixed map was found exactly. In map coefficient space, only affine-equivalent rescalings survived the restricted exact search; no genuinely distinct map family was found.

## References

1. Alpöge, L. (2026, July 20). Public post containing the displayed map and collision. https://xcancel.com/__alpoge__/status/2079028340955197566
2. Bass, H., Connell, E. H., & Wright, D. (1982). The Jacobian conjecture: Reduction of degree and formal expansion of the inverse. Bulletin of the American Mathematical Society, 7(2), 287–330. https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-7/issue-2/The-Jacobian-conjecture--Reduction-of-degree-and-formal-expansion/bams/1183549636.full
3. Jelonek, Z. (1993). The set of points at which a polynomial map is not proper. Annales Polonici Mathematici, 58(3), 259–266. https://eudml.org/doc/262458
4. Adjamagbo, K. (2012). The complete solution to Bass’ generalized Jacobian conjecture. arXiv:1210.5281. https://arxiv.org/abs/1210.5281
5. Rodríguez Díaz, L. O. (2026). On the origin of the Jacobian conjecture. Comptes Rendus Mathématique, 364, 363–370. https://doi.org/10.5802/crmath.831
6. The Stacks Project Authors. Étale morphisms of schemes. https://stacks.math.columbia.edu/tag/024J

## Reproducibility appendix

The accompanying bundle contains:

- investigate_sympy.py — all exact Gröbner, elimination, discriminant, fiber, z-channel, and coefficient-family calculations, with assertions;
- verify_nerdamer.js — independent exact determinant and collision check;
- exact_output_sympy.txt and exact_output_nerdamer.txt — captured textual outputs;
- requirements.txt, package.json, and package-lock.json — pinned dependencies;
- README.md — reproduction commands;
- technical_report.md — plain-text source of this report.

The captured execution completed with “All assertions passed” in SymPy and “All independent exact checks passed” in Nerdamer.

