#!/usr/bin/node
const process = require('process');

if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
}
