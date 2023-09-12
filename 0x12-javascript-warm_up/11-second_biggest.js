#!/usr/bin/node
const arg = process.argv;
if (arg.length === 2 || arg.length === 3) {
  console.log('0');
} else {
  let arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr = arr.sort((a,b) => a - b);
  console.log(arr[arr.length - 2]);
}
