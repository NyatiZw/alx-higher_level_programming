// Use the jquery API to fetch the character data from URL
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data, textStatus) {
	// Extract the character name from the fetched data
	const characterName = data.name;

	// Update <div> text with character
	$('DIV#character').text(data.name);
});
