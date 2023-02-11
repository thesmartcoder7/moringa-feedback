let loginToggle = document.querySelector("#login-toggle");
let signupToggle = document.querySelector("#signup-toggle");

let loginForm = document.querySelector("#login-form");
let signupForm = document.querySelector("#signup-form");

loginToggle.addEventListener("click", () => {
  signupForm.style.display = "none";
  loginForm.style.display = "flex";
});

signupToggle.addEventListener("click", () => {
  loginForm.style.display = "none";
  signupForm.style.display = "flex";
});

