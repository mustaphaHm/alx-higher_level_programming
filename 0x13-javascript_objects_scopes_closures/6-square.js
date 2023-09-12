#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    const ch = c === undefined ? 'X' : 'C';
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += ch;
      }
      console.log(line);
    }
  }
}
module.exports = Square;
