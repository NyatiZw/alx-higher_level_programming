#!/usr/bin/node
// Script that writes a string to a file

const request = require('request');

function countMoviesWithCharacter(apiUrl, characterId) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const filmsData = JSON.parse(body).results;
      const moviesWithCharacter = filmsData.filter((movie) =>
        movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );

      console.log(moviesWithCharacter.length);
    }
  });
}

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error(error);
} else {
  const apiUrl = process.argv[2];
  const characterId = 18;

  countMoviesWithCharacter(apiUrl, characterId);
}
