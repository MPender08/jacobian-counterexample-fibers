# Symbolic investigation of the proposed three-dimensional Jacobian counterexample

This bundle reproduces the exact calculations in the accompanying technical report.
No floating-point arithmetic is used for any mathematical claim.

## Environment

- Python 3.12.13
- SymPy 1.14.0
- Node.js 24.14.0
- Nerdamer 1.1.13

## Reproduction

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python investigate_sympy.py

npm install
node verify_nerdamer.js
```

The Python script performs the Gröbner-basis, elimination, discriminant,
exceptional-locus, exact-fiber, z-channel, and restricted-family calculations.
The JavaScript script independently checks the determinant and reported collision
in a second symbolic algebra system.

## Reliability notes

- The generic eliminant is obtained over the polynomial ring
  `QQ[a,b,c,x,y,z]`, not by clearing denominators in a rational reconstruction.
- Every claimed sample root is checked against all three original equations.
- The loci where the convenient formulas divide by `Q`, `L`, `x`, or `1+xy`
  are handled separately.
- `L=0` is a collision of the projection to the `x` coordinate, not a multiple
  point of the full fiber.
- The restricted family search is exact and limited to the stated ansatz; it is
  not evidence about all nearby polynomial maps.

