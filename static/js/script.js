function main() {
  autoFormSubmit();
  burgerMenu();
}

function autoFormSubmit() {
  const photo_file = document.querySelector(".form-picture__input");
  const form = document.querySelector(".form-picture")

  if (photo_file) {
    photo_file.addEventListener("change", () => form.submit());
  }
}

function burgerMenu() {
  const burger = document.querySelector(".burger");
  const menu = document.querySelector(".nav__list");
  const header = document.querySelector(".header");
  burger.addEventListener("click", () => menu.classList.toggle("menu-active"))
  burger.addEventListener("click", () => header.classList.toggle("header-active"))
}

main();