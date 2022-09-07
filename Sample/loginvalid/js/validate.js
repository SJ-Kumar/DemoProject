const email = document.getElementById("registerEmail");
      const emailError = document.querySelector('#registerEmail + span.error');
    
      const password = document.getElementById("registerPassword").value;
        
      const repass = document.getElementById("registerRepeatPassword");
     
      function validateform(){
        return true;
      }

      email.addEventListener("input", function (event) {
          
        if (email.validity.valid) {
      // In case there is an error message visible, if the field
      // is valid, we remove the error message.
      emailError.innerHTML = ''; // Reset the content of the message
      emailError.className = 'error'; // Reset the visual state of the message
    } else {
      // If there is still an error, show the correct error
      showError();
    }
});

function showError() {
    if(email.validity.valueMissing) {
      
      // If the field is empty
      // display the following error message.
      emailError.textContent = 'You need to enter an e-mail address.';
    } else if(email.validity.typeMismatch) {
      // If the field doesn't contain an email address
      // display the following error message.
      emailError.textContent = 'Entered value must be a valid e-mail address.';
    } else if(email.validity.tooShort) {
      // If the data is too short
      // display the following error message.
      emailError.textContent = `Email should be at least ${ email.minLength } characters; you entered ${ email.value.length }.`;
    }

    // Set the styling appropriately
    emailError.className = 'error active';
  }      