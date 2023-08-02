// Use jquery API to add click event
$('#toggle_header').on('click', function() {
	// Checking header color is red
	if ($('header').hasClass('red')) {
		// remove class red and add class green
		$('header').removeClass('red').addClass('green');
	} else {
		// if class is green remove and add red class
		$('header').removeClass('gree').addClass('red');
	}
});
