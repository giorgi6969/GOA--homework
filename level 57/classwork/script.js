
let person = {
  name: "giorgi",
  surname: "sulaqvelidze",
  academy: "GOA",
  num: 15,
  favColor: "orange",
  isGoaStudent: true,
  

  greet: function() {
    console.log("hello");
  }
};


console.log(person);


console.log(person.favColor);


person.greet();







console.log(true && true);   // true 
console.log(true && false);  // false 
console.log(false && true);  // false
console.log(false && false); // false



console.log(true || true);   // true 
console.log(true || false);  // true 
console.log(false || true);  // true 
console.log(false || false); // false\


const myObj = {
  name: "giorgi",
  age: 10,
  city: "tbilisi",


  printName: function () {
    console.log("name:", this.name);
  },

 
  printAge: function () {
    console.log("age:", this.age);
  },

  
  printCity: function () {
    console.log("city:", this.city);
  }
};


myObj.printName();  
myObj.printAge();   
myObj.printCity();  

