const form = document.getElementById('form');
const username = document.getElementById('registerName');
const email = document.getElementById('registerEmail');
const password = document.getElementById('registerPassword');
const password2 = document.getElementById('registerRepeatPassword');

// success msg
function showSuccess(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control success'
};

// error msg
function showError(input, message) {
    const formControl = input.parentElement;
    formControl.className = 'form-control error';
    
    const small = formControl.querySelector('small');
    small.innerText = message;
};

// email functionality
function isValidEmail(email) {
    const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
};

// event listeners
form.addEventListener('submit', function(e){
    e.preventDefault();

    if(username.value === '') {
        showError(username, 'Required field: "username"');
    }
    else{
        showSuccess(username);
    }


    if(email.value === '') {
        showError(email, 'Required field: "email"');
    }
    else if(!isValidEmail(email.value)) {
        showError(email,'Required field');
    }
    else{
        showSuccess(email);
    }


    if(password.value === '') {
        showError(password, 'Required field: "password"');
    }  
    else {
        showSuccess(password);
    }
    
    
    if(password2.value === '') {
        showError(password2, 'Required field: "password"');
    }
    else if(password2.value !== password.value){
        showError(password2, 'Fields do not match');
    }  
    else {
        showSuccess(password2);
    }  

});