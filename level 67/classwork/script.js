const slides = document.getElementById("slides");
const images = slides.getElementsByTagName("img");
let index = 0;
const total = images.length;

document.getElementById("next").addEventListener("click", function() {
  index = (index + 1) % total;
  slides.style.transform = `translateX(-${index * 600}px)`;
});

document.getElementById("prev").addEventListener("click", function() {
  index = (index - 1 + total) % total;
  slides.style.transform = `translateX(-${index * 600}px)`;
});
