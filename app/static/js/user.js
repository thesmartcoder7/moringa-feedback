let categories = document.querySelectorAll(".main-content");
let links = document.querySelectorAll(".nav");

let commentToggle = document.querySelectorAll(".show-comments");
let upload = document.querySelector(".upload");
let imageUpload = document.querySelector(".upload-image");

let pitch_form = document.querySelector("#share-form");
let menu_toggle = document.querySelector(".image");
let menu = document.querySelector(".navlinks");

for (let i = 0; i < links.length; i++) {
  links[i].addEventListener("click", (e) => {
    if (e.target.textContent === "questions") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "questions") {
          categories[k].classList.add("active");
        }
      }
    } else if (e.target.textContent === "feedback") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "feedback") {
          categories[k].classList.add("active");
        }
      }
    } else {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "shoutouts") {
          categories[k].classList.add("active");
        }
      }
    }
  });
}

for (let i = 0; i < commentToggle.length; i++) {
  commentToggle[i].addEventListener("click", (e) => {
    console.log(e);
    if (
      e.target.parentElement.parentElement.lastElementChild.style.display !=
      "block"
    ) {
      e.target.parentElement.parentElement.lastElementChild.style.display =
        "block";
      e.target.textContent = "Hide Comments";
    } else {
      e.target.parentElement.parentElement.lastElementChild.style.display =
        "none";
      e.target.textContent = "Show Comments";
    }
  });
}

menu_toggle.addEventListener("click", () => {
  menu.style.display = "flex";
  menu.style.animation = "menu_slide_in 0.5s";
  menu.style.left = "0";
});

menu.addEventListener("click", () => {
  menu.style.animation = "menu_slide_out 0.5s";
  menu.style.left = "100%";
  setTimeout(() => {
    menu.style.display = "none";
  }, 500);
});
