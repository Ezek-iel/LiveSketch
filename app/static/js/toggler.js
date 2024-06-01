document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach(el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });

});

document.addEventListener('DOMContentLoaded', () => {
  (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode;

    $delete.addEventListener('click', () => {
      $notification.parentNode.removeChild($notification);
    });
  });
});


// * Function called when navigating to the next stage of the signup
function nextStep() {
  const currentStep = document.querySelector('.step-item.is-active');
  const currentStepContent = document.querySelector(`.step-content[data-step="${currentStep.dataset.step}"]`);

  const nextStep = currentStep.nextElementSibling;
  if (nextStep) {
      currentStep.classList.remove('is-active');
      nextStep.classList.add('is-active');

      currentStepContent.classList.add('step-content-exit-active');
      currentStepContent.addEventListener('transitionend', () => {
          currentStepContent.style.display = 'none';
          currentStepContent.classList.remove('step-content-exit-active');

          const nextStepContent = document.querySelector(`.step-content[data-step="${nextStep.dataset.step}"]`);
          nextStepContent.style.display = 'block';
          nextStepContent.classList.add('step-content-enter');
          setTimeout(() => {
              nextStepContent.classList.remove('step-content-enter');
          }, 10);
      }, { once: true });
  }
}


//* Function called when navigating to the previous stage of the signup
function prevStep() {
  const currentStep = document.querySelector('.step-item.is-active');
  const currentStepContent = document.querySelector(`.step-content[data-step="${currentStep.dataset.step}"]`);

  const prevStep = currentStep.previousElementSibling;
  if (prevStep) {
      currentStep.classList.remove('is-active');
      prevStep.classList.add('is-active');

      currentStepContent.classList.add('step-content-enter-active');
      currentStepContent.addEventListener('transitionend', () => {
          currentStepContent.style.display = 'none';
          currentStepContent.classList.remove('step-content-enter-active');

          const prevStepContent = document.querySelector(`.step-content[data-step="${prevStep.dataset.step}"]`);
          prevStepContent.style.display = 'block';
          prevStepContent.classList.add('step-content-exit');
          setTimeout(() => {
              prevStepContent.classList.remove('step-content-exit');
          }, 10);
      }, { once: true });
  }
}

function validateAccountStep() {

    let emailAddress = document.getElementById("emailInput").value;
    let emailRemark = document.getElementById("emailError")

    let password = document.getElementById("passwordInput").value;
    let passwordRemark = document.getElementById("passwordError")

    let passwordConfirm = document.getElementById("passwordConfirmInput").value
    let passwordConfirmRemark = document.getElementById("passwordConfirmError")

    
    //* Validating email address
    if (emailAddress.length < 8){
        emailRemark.textContent = "Email Address must be 8 characters or more"
    }else{
      emailRemark.textContent = ""
    }

    //* validating password
    if (password.length < 8){
      passwordRemark.textContent = "Password Must be 8 characters or more"
    }else{
      passwordRemark.textContent = ""
    }
    
    //* validating password confirm
    if (password !== passwordConfirm){
      passwordConfirmRemark.textContent = "Confirm password must be equal to password"
    }else{
      passwordConfirmRemark.textContent = ""
    }

    if (emailAddress.length >= 8 && password.length >= 8 && password === passwordConfirm){
      nextStep()
    }
}

function validateProfileStep() {
  let username = document.getElementById("usernameInput").value
  let usernameRemark = document.getElementById("usernameError")

  let displayName = document.getElementById("displayNameInput").value
  let displayNameRemark = document.getElementById("displayNameError")
  

  if (username.length < 8){
    usernameRemark.textContent = "Username must be 8 characters or more"
  }
  else{
    usernameRemark.textContent = ""
  }

  if (displayName.length < 5){
    displayNameRemark.textContent = "Display Name must be 5 characters or more"
  }
  else{
    usernameRemark.textContent = ""
  }

  if (username.length >= 8 && displayName.length >= 5){
    nextStep()
  }

}