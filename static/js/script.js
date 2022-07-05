function main() {
  autoFormSubmit();
}

function autoFormSubmit() {
  const photo_file = document.querySelector(".form-picture__input");
  const form = document.querySelector(".form-picture")

  if (photo_file) {
    photo_file.addEventListener("change", () => form.submit());
  }
}

main();