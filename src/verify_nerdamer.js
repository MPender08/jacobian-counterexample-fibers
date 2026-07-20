#!/usr/bin/env node
// Independent exact check in Nerdamer 1.1.13.

const nerdamer = require('nerdamer/all');

const F1 = '(1+x*y)^3*z+y^2*(1+x*y)*(4+3*x*y)';
const F2 = 'y+3*x*(1+x*y)^2*z+3*x*y^2*(4+3*x*y)';
const F3 = '2*x-3*x^2*y-x^3*z';
const functions = [F1, F2, F3];

const derivative = (f, variable) => nerdamer(`diff(${f},${variable})`).toString();
const J = functions.map(f => ['x', 'y', 'z'].map(v => derivative(f, v)));
const det =
  `(${J[0][0]})*((${J[1][1]})*(${J[2][2]})-(${J[1][2]})*(${J[2][1]}))` +
  `-(${J[0][1]})*((${J[1][0]})*(${J[2][2]})-(${J[1][2]})*(${J[2][0]}))` +
  `+(${J[0][2]})*((${J[1][0]})*(${J[2][1]})-(${J[1][1]})*(${J[2][0]}))`;

const determinant = nerdamer(`expand(${det})`).toString();
console.log('Nerdamer version: 1.1.13');
console.log('det(JF) =', determinant);
if (determinant !== '-2') throw new Error(`Unexpected determinant: ${determinant}`);

const points = [
  {x: 0, y: 0, z: '-1/4'},
  {x: 1, y: '-3/2', z: '13/2'},
  {x: -1, y: '3/2', z: '13/2'},
];
for (const point of points) {
  const image = functions.map(f => nerdamer(f, point).evaluate().text('fractions'));
  console.log(`F(${point.x},${point.y},${point.z}) = (${image.join(',')})`);
  if (image.join(',') !== '-1/4,0,0') throw new Error(`Unexpected image: ${image}`);
}
console.log('All independent exact checks passed.');

