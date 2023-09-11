#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg) || arg === 1) {
  console.log(0);
} else {
  let arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr = arr.sort();
  console.log(arr[arr.length - 2]);
}
