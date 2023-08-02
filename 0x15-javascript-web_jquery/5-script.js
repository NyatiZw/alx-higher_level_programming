//Use jquery to add a click event
$('#add_item').on('click', function() {
	//Create a new <li> element
	const newItem = $('<li>').text('Item');

	// Append the new <li> element to list
	$('.my_list').append(newItem);
});
