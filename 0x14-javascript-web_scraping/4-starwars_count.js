#!/usr/bin/node
const axios = require('axios').default;
const URL = process.argv[2];

axios.get(URL)
  .then((response) => {
    const films = response.data['results'];
    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch((error) => {
    console.log(error);
  });
