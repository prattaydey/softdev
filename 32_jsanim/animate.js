// Team PeanutButter: Prattay Dey, Brian Yang
// SoftDev pd07
// K32 -- JSanim
// 2023-04-26

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
    //e.preventDefault();
    //IDK WHAT THIS IS
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
  clear(ctx);

  var rectWidth = 60;
  var rectHeight = 40;

  // (x,y) upper left corner of image
  var rectX = Math.floor( Math.random() * 440);
  var rectY = Math.floor( Math.random() * 460);

  var xVel = -1;
  var yVel = -1;

  var logo = new Image();
  logo.src = "logo_dvd.jpg";

  var dvdLogo = () => {
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    if (rectX == 0 || rectX == 440) {
      xVel = xVel * -1;
    }
    if (rectY == 0 || rectY == 460) {
      yVel = yVel * -1;
    }
    rectX += xVel;
    rectY += yVel;
    requestID = window.requestAnimationFrame(dvdLogo);
  }
  dvdLogo();
}

var stopIt = () => {
  console.log("stopIt invoked...");
  console.log( requestID );

  window.cancelAnimationFrame( requestID );
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup)
stopButton.addEventListener("click", stopIt);
