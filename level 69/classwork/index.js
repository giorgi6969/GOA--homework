let number = prompt("enter number:");

number = Number(number); 

if (number % 2 === 0) {
  console.log("is number luwi");
} else {
  console.log("is number kenti");
}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Show / Hide Photo</title>
</head>
<body>

 
  <img id="myPhoto" src="photo.jpg" style="display: none;" alt="photo ">

  <br><br>

  
  <button onclick="showPhoto()">Show</button>
  <button onclick="hidePhoto()">Hide</button>

  
  

</body>
</html>

 
    function showPhoto() {
      document.getElementById("myPhoto").style.display = "block";
    }

    function hidePhoto() {
      document.getElementById("myPhoto").style.display = "none";
    }
 
