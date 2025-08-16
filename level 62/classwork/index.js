
const heading = document.getElementById("myHeading");


function changeFontSize() {
  const userInput = prompt("enter a number (px):");
  const size = parseInt(userInput); 

  if (!isNaN(size) && size > 0) {
    heading.style.fontSize = size + "px";
  } else {
    alert("Please enter a positive number!");
  }
}


heading.addEventListener("click", changeFontSize);
<!DOCTYPE html>
<html lang="ka">
<head>
  <meta charset="UTF-8">a
  <title>document</title>
</head>
<body>


  <img id="myImage" src="" alt="photo">

  <script src="script.js"></script>
</body>
</html>

