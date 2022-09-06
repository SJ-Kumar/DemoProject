<script>
			function NEXSEEDS() {
				var name =
					document.forms.RegForm.Name.value;
                var username =
                    document.forms.RegForm.Username.value;
                var registerNo =
                    document.forms.RegForm.RegisterNo.value;
				var email =
					document.forms.RegForm.EMail.value;
				var mobile =
					document.forms.RegForm.MobileNo.value;
				var password =
					document.forms.RegForm.Password.value;
                var re-enterpassword =
					document.forms.RegForm.Re-enter Password.value;
				var regEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g;
				var regPhone=/^\d{10}$/;							
				var regName = /\d+$/g;

				if (name == "" || regName.test(name)) {
					window.alert("Please enter your name properly.");
					name.focus();
					return false;
				}
				
				if (email == "" || !regEmail.test(email)) {
					window.alert("Please enter a valid e-mail address.");
					email.focus();
					return false;
				}
				
				if (password == "") {
					alert("Please enter your password");
					password.focus();
					return false;
				}

				if(password.length <6){
					alert("Password should be atleast 6 character long");
					password.focus();
					return false;

                if(re-enterpassword!==password){
                        alert("re entered Password should be same as password");
                        re-enterpassword.focus();
                        return false;

				}
				if (mobile == "" || !regPhone.test(mobile)) {
					alert("Please enter valid phone number.");
					mobile.focus();
					return false;
				}


				return true;
			}
        </script>
