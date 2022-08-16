#!/usr/bin/node
const process = require('process');
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const string = 'X';
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(string.repeat(process.argv[2]));
  }
}
