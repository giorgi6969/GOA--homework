//  console.log(5 > 3)       //True
// console.log(7 < 10)     //True
// console.log(4 >= 4)    // True
// console.log(6 <= 8)    // True
// console.log(9 == 9)   // True
// console.log(3 != 5)   //True
// console.log(4 == 4)   // True
// console.log(5 == 5)   // True
// console.log(15 == 15) //True
// console.log(32 == 32) // True


    function handleSubmit(event) {
      event.preventDefault();

      const form = document.getElementById('myForm');

      const firstName = form.elements['firstName'].value;
      const lastName = form.elements['lastName'].value;
      const email = form.elements['email'].value;
      const age = form.elements['age'].value;

      console.log('First Name:', firstName);
      console.log('Last Name:', lastName);
      console.log('Email:', email);
      console.log('Age:', age);

      form.reset();
    }
 

 

