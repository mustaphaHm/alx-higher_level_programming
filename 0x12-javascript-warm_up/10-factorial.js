#!/usr/bin/node
const arg = parseInt(process.argv[2]);
console.log(fact(arg));
function fact (a) {
  if (a === 1 || isNaN(a)) {
    return (1);
  }
  return (a * fact(a - 1));
}
