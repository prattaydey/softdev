// Team PreView :: Prattay Dey, Verit Li
// SoftDev pd07
// K32 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.strokeStyle = "#000000"; // black outline
ctx.fillStyle = "#00ffff"; // cyan

// init global var for use w animation frames
var requestID;

var clear = (e) => {
    e.preventDefault(); // 
    ctx.clearRect(0, 0, e.width, e.height);
}

var radius = 0;
var growing = true;

var drawDot = () => {
    // canceling frame prevents speeding up
    window.cancelAnimationFrame( requestID );
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
      else{
        radius -= 1;
      }
    }
     
}

var dvdLogoSetup = () => {
    window.cancelAnimationFrame( requestID );

    var rectWidth = 60;
    var rectHeight = 40;

    var RectX = Math.floor( Math.random() * 380);
    var RectY = Math.floor( Math.random() * 420);

    var xVel = 2;
    var yVel = 2;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = () => {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(rectX, rectY, rectWidth, rectHeight);
        if ( rectX == 0 || rectX == 440){
            
        }
    }

}

var stopIt = () => {
  console.log("stopIt invoked...");
  console.log( requestID );

  window.cancelAnimationFrame( requestID );
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
