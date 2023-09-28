#!/usr/bin/node
const request = require('request');
const titleId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${titleId}`;
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err.message);
  } else {
    const title = JSON.parse(body);
    const characterUrls = title.characters;
    fetchCharacterNamesInOrder(characterUrls, 0);
  }
});

function fetchCharacterNamesInOrder (charUrls, index) {
  request.get(charUrls[index], (err, response, body) => {
    if (err) {
      console.error('Error:', err.message);
      return;
    }
    const character = JSON.parse(body);
    console.log(character.name);
    if (index + 1 < charUrls.length) {
      fetchCharacterNamesInOrder(charUrls, index + 1);
    }
  });
}
