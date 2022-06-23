function main() {
  autoFormSubmit();
}

function autoFormSubmit() {
  const photo_file = document.querySelector(".main__input");
  const form = document.querySelector(".main__form")

  photo_file.addEventListener("change", () => form.submit());
}

main();