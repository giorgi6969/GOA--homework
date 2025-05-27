 document.getElementById("ID1").addEventListener("submit", function(event) {
      event.preventDefault(); 

      const input1 = document.getElementById("input1").value;
      const input2 = document.getElementById("input2").value;
      const input3 = document.getElementById("input3").value;

      console.log("name:", input1);
      console.log("surname:", input2);
      console.log("gmail:", input3);
    });