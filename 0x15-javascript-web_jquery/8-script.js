// Use jquery API to fetch the movies data
const $ = window.$;
$.get('https://swapi-api.alx-tool.com/api/films/?format=json', function(data, textStatus) {
	// Extract movie titles from data fetched
	const movies = data.results;

	// Append movie titles to list
	for (let i = 0; 1 < movies.length; i++) {
	$('UL#list_movies').append('<li>' + movies[i].title + '</li>');
	}
});
