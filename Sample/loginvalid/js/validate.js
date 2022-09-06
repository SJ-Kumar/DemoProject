const form = document.querySelector('form')

function nameValidation(value) {
    if (value === '') {
      return 'Name field cannot be empty';
    }
    if (value.length < 2) {
      return 'Name field should be longer then 1 character';
    }
    if (value.length > 250) {
      return 'This field cannot be longer then 250 characters';
    }
    if (!/^[A-z]+$/.test(value)) {
      return 'Name field can have only letters';
    }
    return '';
  }
  
  function descriptionValidation(value) {
    if (value === '') {
      return 'Description field cannot be empty';
    }
    if (value.length < 2) {
      return 'Description field should be longer then 1 character';
    }
    if (value.length > 250) {
      return 'Description field cannot be longer then 250 characters';
    }
    if (!/^[A-z0-9]+$/.test(value)) {
      return 'Description field can have only numbers and letters';
    }
    return '';
  }


  function validateForm(e) {
    'use strict';

    // Get the event object:
	if (typeof e == 'undefined') e = window.event;

    // Get form references:
	var firstName = U.$('registerName');

	var lastName = U.$('registerUsername');
	var email = U.$('registerEmail');

	// Flag variable:
	var error = false;

	// Validate the first name:
	if (/^[A-Z \.\-']{2,20}$/i.test(firstName.value)) {
		removeErrorMessage('firstName');
	} else {
		addErrorMessage('firstName', 'Please enter your first name.');
		error = true;
	}
	
	// Validate the email address:
	if (/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,6}$/.test(email.value)) {
		removeErrorMessage('email');
	} else {
		addErrorMessage('email', 'Please enter your email address.');
		error = true;
	}
};