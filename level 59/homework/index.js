
console.log(String(123));     
console.log(String(true));     
console.log(Number("456"));    
console.log(Number(false));    
console.log(Number("hello")); 


let num = Number(prompt("Enter a number:"));

if (num > 0) {
  alert("The number is positive.");
} else if (num < 0) {
  alert("The number is negative.");
} else {
  alert("The number is zero.");
}
let age = Number(prompt("Enter your age:"));

if (age >= 18) {
  alert("You can vote!");
} else {
  alert("You are not eligible to vote.");
}
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));

if (num1 > num2) {
  alert("First number is larger");
} else if (num2 > num1) {
  alert("Second number is larger");
} else {
  alert("Both numbers are equal");
}
let person = {}; 

person.name = "giorgi";
person.age = 10;
person.city = "Tbilisi";

console.log(person.name);

person.hobby = "Reading";        
person.city = "Batumi";        
console.log(person); 
