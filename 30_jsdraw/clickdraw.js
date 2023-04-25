// Team Peanut Butter :: Prattay Dey, Brian Yang
// SoftDev pd07
// K30 -- JS Paint
// 2023-04-24

// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// init global state var
var mode = "rect";

// var toggleMode = function(e) {
 var toggleMode = (e) => {
     console.log("toggling...");
     if (mode == "rect") {
       mode = "circle"
       bToggler.innerHTML = "circle"
     }
     else {
       mode = "rect"
       bToggler.innerHTML = "rect"

     }
 }

var drawRect = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle="#ff0000";
    ctx.fillRect(mouseX, mouseY, 100,200);
}

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle="#ff0000";
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill();
}

// checks if mode is rect or circle, then calls the respective draw function
var draw = (e) => {
    if (mode == "rect"){
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
