// Use the jquery API to fetch the data from URL
$.getJson('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
	// Extract the translation of "hello"
	const translation = data.hello;

	// Update the text of the <div> element
	$('#hello').text(translation);
});
