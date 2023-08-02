// Use jquery API to fetch the movies data
$.getJson('https://swapi-api.alx-tool.com/api/films/?format=json', function(data) {
	// Extract movie titles from data fetched
	const movies = data.results;
	const movieTitles = movies.map(movie => movie.title);

	// Append movie titles to list
	const listElement = $('#list_movies');
	$.each(movieTitles, function(index, title) {
		listElement.append(`<li>${title}</li>`);
	});
});
