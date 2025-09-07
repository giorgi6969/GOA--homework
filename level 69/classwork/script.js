const heading = document.getElementById("myHeading");

heading.addEventListener("pointerdown", function(e) {

  if (e.target.style.fontSize === "30px") {
    e.target.style.fontSize = "20px";
  } else {
    e.target.style.fontSize = "30px";
  }

});