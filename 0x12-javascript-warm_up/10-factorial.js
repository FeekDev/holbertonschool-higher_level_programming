#!/usr/bin/node
const process = require('process');
factorialize();

function factorialize (num) {
  num = parseInt(process.argv[2]);
  let result = num;
  if (num <= 0) {
    return 1;
  } else {
    while (num > 1) {
      num--;
      result *= num;
    }
    console.log(result);
  }
}
