#!/usr/bin/node
const arguments = process.argv.length;
console.log(arguments === 2 ? 'No argument' : (arguments === 3 ? 'Argument found' : 'Arguments found'))

