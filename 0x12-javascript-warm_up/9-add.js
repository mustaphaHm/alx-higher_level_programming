#!/usr/bin/node
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
add(x, y);
function add (a, b) {
  console.log(a + b);
}
