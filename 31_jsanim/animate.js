// Team PreView :: Prattay Dey, Verit Li
// SoftDev pd07
// K31 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.strokeStyle = "#000000"; // black outline
ctx.fillStyle = "#00ffff"; // cyan

// init global var for use w animation frames
var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, e.width, e.height);
}

var radius = 0;
var growing = true;

var drawDot = () => {
    requestID = window.requestAnimationFrame(drawDot);
    // wipes canvas
    clear(c);
    //repaints circle
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();

    if (growing){
      if (radius > c.width/2){
        growing = false;
      }
      radius += 1;
    }
    else{
      if (radius == 0){
        growing = true;
      }
      radius -= 1;
    }
     
}

var stopIt = () => {
  console.log("stopIt invoked...");
  console.log( requestID );

  window.cancelAnimationFrame( requestID );
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
