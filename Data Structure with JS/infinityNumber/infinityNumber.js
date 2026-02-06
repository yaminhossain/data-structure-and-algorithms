//In JavaScript, you can declare or obtain infinity using the global "Infinity" property, properties on the "Number" object.

let positiveInfinity = Infinity;
let negativeInfinity = -Infinity;

if (Math.pow(10, 900) > positiveInfinity) {
  console.log("True");
}
else{
  console.log("False");
}

//Using number object
// let positiveInfinity = Number.POSITIVE_INFINITY;
// let negativeInfinity = Number.NEGATIVE_INFINITY;
