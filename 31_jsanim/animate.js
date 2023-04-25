// Team PreView :: Prattay Dey, Verit Li
// SoftDev pd07
// K31 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#00ffff";

// init global var for use w animation frames
var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, e.width, e.height);
}

var radius = 0;
var growing = true;

var drawDot = () => {
    // wipes canvas
    clear(c);
    //repaints circle
    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, 2 * Math.PI);
    ctx.fill();
    // window.cancelAnimationFrame(requestID)
    // window.requestAnimationFrame(drawDot)


}