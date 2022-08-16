#!/usr/bin/node
const process = require('process');
let string = '';
let i;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      string += 'x';
    }
    if (i < (process.argv[2] - 1)) {
      string += '\n';
    }
  }
  console.log(string);
}
