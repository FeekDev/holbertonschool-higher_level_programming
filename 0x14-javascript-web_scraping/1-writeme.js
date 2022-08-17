#!/usr/bin/node
const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3],
  {
    enconding: 'utf-8'
  },
  (err) => {
    if (err) throw err;
  });
