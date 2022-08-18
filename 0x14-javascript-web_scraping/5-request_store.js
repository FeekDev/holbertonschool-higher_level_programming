#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const URL = process.argv[2];
const path = process.argv[3];

async function StoreBody () {
  try {
    const response = await axios.get(URL);
    fs.writeFile(path, response.data,
      {
        enconding: 'utf-8'
      },
      (err) => {
        if (err) throw err;
      });
  } catch (error) {
    console.error(error);
  }
}

StoreBody();
