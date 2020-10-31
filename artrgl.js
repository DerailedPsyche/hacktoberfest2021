// JavaScript program to find the area of a triangle

let side1 = prompt('Enter side1: ');
let side2 = prompt('Enter side2: ');
let side3 = prompt('Enter side3: ');

// calculate the semi-perimeter
let s = (side1 + side2 + side3) / 2;

//calculate the area
let areaValue = Math.sqrt(
  s * (s - side1) * (s - side2) * (s - side3)
);

console.log(
  `The area of the triangle is ${areaValue}`
);
