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
// var toggleMode = (e) => {
//     console.log("toggling...");
//     if () {

//     }
//     else {

//     }
// }

var drawRect = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

}

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
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
    
}

c.addEventListener("click", draw);
// var bToggler = document. ;
// bToggler. ;
// var clearB = ;
// clearB. ;

