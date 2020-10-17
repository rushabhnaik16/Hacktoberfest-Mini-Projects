var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");

//console.log(color1.value);

function setGradient() {
    body.style.background = 
    "linear-gradient(to right, "
     + color1.value 
     + ", " 
     + color2.value 
     + ")";
}
//console.log(body);
color1.addEventListener("input" , setGradient);
color2.addEventListener("input" , setGradient);
