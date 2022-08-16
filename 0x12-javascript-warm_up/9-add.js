#!/usr/bin/node
const process = require('process');
add();

function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];
  console.log(parseInt(a) + parseInt(b));
}
