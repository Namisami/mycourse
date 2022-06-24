function main() {
  autoFormSubmit();
}

function autoFormSubmit() {
  const photo_file = document.querySelector(".new__input");
  const form = document.querySelector(".new")

  photo_file.addEventListener("change", () => form.submit());
}

main();