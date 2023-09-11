#!/usr/bin/node
const first = parseInt(process.argv[2]);
console.log(isNaN(first) ? 'Not a number' : 'My number: ' + first);
