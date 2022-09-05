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
