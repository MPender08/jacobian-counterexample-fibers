#!/usr/bin/env python3
"""Exact symbolic investigation of the Alpoge–Fable Jacobian map.

Requires Python 3.12+ and SymPy 1.14.0.  All arithmetic is exact.
The script prints exact results and performs assertion-based validation.
"""

from __future__ import annotations

import platform
import sys
from pathlib import Path

import sympy as sp


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


x, y, z, a, b, c = sp.symbols("x y z a b c")
u = 1 + x * y

F1 = u**3 * z + y**2 * u * (4 + 3 * x * y)
F2 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
F3 = 2 * x - 3 * x**2 * y - x**3 * z
F = sp.Matrix([F1, F2, F3])

Q = 27 * a**2 * c**2 - 18 * a * b * c + 16 * a + b**3 * c - b**2
R = 4 - 3 * b * c
L = 27 * a * c**2 - 9 * b * c + 8
P = sp.expand(Q * x**3 + R * x - 2 * c)


def exact_tuple(point):
    subs = dict(zip((x, y, z), point))
    return tuple(sp.factor(fi.subs(subs)) for fi in F)


def reduced_basis(target, variables=(z, y, x)):
    aa, bb, cc = target
    return sp.groebner(
        [F1 - aa, F2 - bb, F3 - cc],
        *variables,
        order="lex",
        domain=sp.QQ,
    )


def main() -> None:
    section("Environment")
    print("Python:", sys.version.replace("\n", " "))
    print("Platform:", platform.platform())
    print("SymPy:", sp.__version__)

    section("Phase 1: determinant and reported collision")
    determinant = sp.factor(F.jacobian([x, y, z]).det())
    print("det(JF) =", determinant)
    assert determinant == -2

    points = [
        (0, 0, -sp.Rational(1, 4)),
        (1, -sp.Rational(3, 2), sp.Rational(13, 2)),
        (-1, sp.Rational(3, 2), sp.Rational(13, 2)),
    ]
    for point in points:
        image = exact_tuple(point)
        print(f"F{point} = {image}")
        assert image == (-sp.Rational(1, 4), 0, 0)

    special = reduced_basis((-sp.Rational(1, 4), 0, 0))
    print("Reduced Groebner basis, lex z > y > x:")
    for polynomial in special.polys:
        print(" ", sp.factor(polynomial.as_expr()))
    expected = [
        x * (x - 1) * (x + 1),
        2 * y + 3 * x,
        4 * z + 1 - 27 * x**2,
    ]
    for polynomial in expected:
        assert special.reduce(polynomial)[1] == 0
    print("All three proposed generators reduce to zero modulo the basis.")

    section("Phase 2: generic elimination")
    generic = sp.groebner(
        [F1 - a, F2 - b, F3 - c],
        z,
        y,
        x,
        a,
        b,
        c,
        order="lex",
        domain=sp.QQ,
    )
    elimination = [
        sp.factor(g.as_expr())
        for g in generic.polys
        if not (g.as_expr().has(y) or g.as_expr().has(z))
    ]
    print("Elimination generators in QQ[a,b,c,x]:")
    for polynomial in elimination:
        print(" ", polynomial)
    assert len(elimination) == 1
    assert sp.factor(27 * elimination[0] - P) == 0
    print("Primitive eliminant P(x) =")
    print(" ", P)
    print("Leading coefficient Q =", Q)
    print("Linear coefficient R =", R)

    discriminant = sp.factor(sp.discriminant(P, x))
    identity = sp.factor(R**3 + 27 * Q * c**2 - L**2)
    print("Discriminant_x(P) =", discriminant)
    print("R^3 + 27 Q c^2 - L^2 =", identity)
    assert discriminant == -4 * L**2 * Q
    assert identity == 0
    assert sp.factor(P.subs({a: F1, b: F2, c: F3})) == 0
    print("Direct identity P(F1,F2,F3;x) = 0 verified.")

    section("Exact family containing the reported collision")
    aa, rr = sp.symbols("aa rr", nonzero=True)
    family_points = [
        (0, 0, aa),
        (rr, 6 * aa * rr, -26 * aa),
    ]
    family_relation = 4 * aa * rr**2 + 1
    print("Target: (aa,0,0), aa != 0")
    print("Point 1: (0,0,aa)")
    print("Points 2/3: (rr,6*aa*rr,-26*aa), where 4*aa*rr^2+1=0")
    for point in family_points:
        vals = [sp.factor(expr) for expr in exact_tuple(point)]
        reduced = [sp.rem(sp.Poly(v - t, rr), sp.Poly(family_relation, rr)).as_expr()
                   if v.has(rr) else sp.factor(v - t)
                   for v, t in zip(vals, (aa, 0, 0))]
        assert all(sp.factor(v) == 0 for v in reduced)
    print("Family validated exactly modulo 4*aa*rr^2+1.")

    section("Exceptional-locus classification")
    print("Q =", Q)
    print("L =", L)
    print("R =", R)
    print("Generic open set Q*L != 0: three distinct x-roots; unique y,z lift per root.")
    print("Q = 0, R != 0: eliminant becomes linear; one full solution.")
    print("Q = R = 0: empty fiber. Equivalent curve:")
    print("  b = 4/(3c), a = 4/(27c^2), c != 0")
    print("L = 0, Q != 0: repeated x-root, but three reduced full points.")

    # Exact L=0 sample: the repeated x-root splits into two y,z solutions.
    l_sample = (-sp.Rational(8, 27), 0, 1)
    l_basis = reduced_basis(l_sample)
    print("Reduced basis at L=0 sample (-8/27,0,1):")
    for polynomial in l_basis.polys:
        print(" ", sp.factor(polynomial.as_expr()))
    l_solutions = sp.solve(
        [F1 - l_sample[0], F2, F3 - 1], [x, y, z], dict=True
    )
    assert len(l_solutions) == 3
    for solution in l_solutions:
        print(" ", {k: sp.factor(v) for k, v in solution.items()})
        assert all(sp.simplify(fi.subs(solution) - ti) == 0
                   for fi, ti in zip(F, l_sample))

    empty_basis = reduced_basis((sp.Rational(4, 27), sp.Rational(4, 3), 1))
    unique_basis = reduced_basis((0, 0, 2))
    print("Basis on missing-image curve at (4/27,4/3,1):",
          [g.as_expr() for g in empty_basis.polys])
    print("Basis at Q=0,R!=0 target (0,0,2):",
          [g.as_expr() for g in unique_basis.polys])
    assert [g.as_expr() for g in empty_basis.polys] == [1]
    assert [g.as_expr() for g in unique_basis.polys] == [z, y, x - 1]

    section("Additional exact target samples")
    samples = [
        (-1, 0, 0),
        (-sp.Rational(1, 9), 0, 0),
        (-4, 0, 0),
        (1, 0, 0),
        (2, 1, 1),
    ]
    for target in samples:
        basis = reduced_basis(target)
        print("Target", target)
        for polynomial in basis.polys:
            print(" ", sp.factor(polynomial.as_expr()))

    # For the irreducible rational sample, validate the lift modulo its cubic.
    target = (2, 1, 1)
    cubic = 104 * x**3 + x - 2
    y_lift = (-5304 * x**2 + 624 * x + 19) / 106
    z_lift = (4680 * x**2 + 96720 * x - 29491) / 424
    for fi, ti in zip(F, target):
        numerator = sp.together(fi.subs({y: y_lift, z: z_lift}) - ti).as_numer_denom()[0]
        assert sp.rem(sp.Poly(numerator, x), sp.Poly(cubic, x)) == 0
    print("All three roots of 104*x^3+x-2 lift to the full target (2,1,1).")

    section("Phase 3: exact z-channel determinant decomposition")
    A = sp.Matrix([
        y**2 * u * (4 + 3 * x * y),
        y + 3 * x * y**2 * (4 + 3 * x * y),
        2 * x - 3 * x**2 * y,
    ])
    B = sp.Matrix([u**3, 3 * x * u**2, -x**3])
    triple = lambda v1, v2, v3: sp.factor(sp.det(sp.Matrix.hstack(v1, v2, v3)))
    terms = {
        "det(Ax,Ay,B)": triple(A.diff(x), A.diff(y), B),
        "det(Bx,Ay,B)": triple(B.diff(x), A.diff(y), B),
        "det(Ax,By,B)": triple(A.diff(x), B.diff(y), B),
        "det(Bx,By,B)": triple(B.diff(x), B.diff(y), B),
    }
    for name, value in terms.items():
        print(name, "=", value)
    assert terms["det(Ax,Ay,B)"] == -2
    assert terms["det(Bx,Ay,B)"] + terms["det(Ax,By,B)"] == 0
    assert terms["det(Bx,By,B)"] == 0
    cone_relation = sp.factor(B[1]**3 + 27 * B[0]**2 * B[2])
    print("B2^3 + 27*B1^2*B3 =", cone_relation)
    assert cone_relation == 0

    print("Division-free elimination of z uses (T-A) cross B = 0:")
    T = sp.Matrix([a, b, c])
    V = T - A
    for i, j in ((0, 1), (0, 2), (1, 2)):
        minor = sp.factor(V[i] * B[j] - V[j] * B[i])
        print(f" minor {i+1}{j+1} =", minor)

    section("Phase 4: restricted coefficient families")
    pp, qq, rrcoef = sp.symbols("p q r")
    scaled = sp.Matrix([
        A[0] + pp * B[0] * z,
        A[1] + qq * B[1] * z,
        A[2] + rrcoef * B[2] * z,
    ])
    scaled_det = sp.Poly(sp.expand(scaled.jacobian([x, y, z]).det()), x, y, z)
    nonconstant = [coefficient for monomial, coefficient in scaled_det.terms()
                   if monomial != (0, 0, 0)]
    scale_constraints = sp.groebner(nonconstant, pp, qq, rrcoef, order="lex")
    print("Independent z-channel scalings: determinant is constant iff")
    for polynomial in scale_constraints.polys:
        print(" ", sp.factor(polynomial.as_expr()))
    print("Constant term =", sp.factor(scaled_det.coeff_monomial(1)))

    h, m, n, pcoef, scoef, k = sp.symbols("h m n pcoef scoef k")
    uh = h + x * y
    ansatz = sp.Matrix([
        uh**3 * z + y**2 * uh * (m + n * x * y),
        y + pcoef * x * uh**2 * z + pcoef * x * y**2 * (m + n * x * y),
        scoef * x - pcoef * x**2 * y + k * x**3 * z,
    ])
    ansatz_det = sp.Poly(sp.expand(ansatz.jacobian([x, y, z]).det()), x, y, z)
    equations = [coefficient for monomial, coefficient in ansatz_det.terms()
                 if monomial != (0, 0, 0)]
    constraints = sp.groebner(equations, h, m, n, pcoef, scoef, k, order="lex")
    print("Six-coefficient ansatz Groebner constraints (before h*s != 0 case split):")
    for polynomial in constraints.polys:
        print(" ", sp.factor(polynomial.as_expr()))
    print("Constant determinant =", sp.factor(ansatz_det.coeff_monomial(1)))
    solution = {
        k: -scoef**2 / 4,
        m: 8 / scoef,
        n: 6 / (h * scoef),
        pcoef: 3 * scoef / (2 * h),
    }
    specialized_det = sp.factor(ansatz_det.as_expr().subs(solution))
    print("On h*s != 0 component:")
    print(" k=-s^2/4, m=8/s, n=6/(h*s), p=3*s/(2*h)")
    print(" determinant =", specialized_det)
    assert specialized_det == -h**3 * scoef
    print("This entire two-parameter family is diagonally equivalent to the original:")
    print(" F_{h,s} = diag(2h^3/s,h,s/2) o F o diag(1,1/h,s/2).")

    section("All assertions passed")


if __name__ == "__main__":
    main()

