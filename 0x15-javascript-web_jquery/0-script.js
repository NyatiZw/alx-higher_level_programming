#!/usr/bin/javascript
// Function to change the text color of the heaader element
function changeHeaderTextColor() {
	// Select the header element using document.querySelector
	const headerElement = document.querySelector('header');

	// Update the text color to red
	headerElement.style.color = '#FF0000';
}

// Call the function
changeHeaderTextColor();
