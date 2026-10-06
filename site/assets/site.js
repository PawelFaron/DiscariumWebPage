/* Progressive enhancement only: navigation, support and policies work without JS. */
document.querySelectorAll("[data-gallery]").forEach((gallery) => {
  const controls = gallery.querySelector(".gallery-controls");
  const image = gallery.querySelector("img");
  const caption = gallery.querySelector("figcaption");
  const buttons = [...controls.querySelectorAll("button")];
  controls.hidden = false;
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      image.src = button.dataset.galleryImage;
      image.alt = button.dataset.galleryAlt;
      caption.textContent = button.dataset.galleryCaption;
      buttons.forEach((item) =>
        item.setAttribute("aria-pressed", String(item === button)),
      );
    });
  });
});
