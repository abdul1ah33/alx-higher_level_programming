#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results;

    for (let i = 0; i < films.length; i++) {
      const film = films[i];
      const characters = film.characters;

      for (let j = 0; j < characters.length; j++) {
        const character = characters[j];

        if (character.includes(characterId)) {
          count += 1;
        }
      }
    }

    console.log(count);
  }
});

