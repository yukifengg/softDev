/*Team Ringbearers :: Frodo Baggins, Bilbo Baggins
SoftDev pd0
K31 -- canvas based JS animation
2023-04-25t

JS file for JavaScript canvas work
*/
var c = document.getElementById("playground"); //get canvas
var dotButton = document.getElementById("buttonCircle"); //get dot button
var stopButton = document.getElementById("buttonStop"); //get stop button

var ctx = c.getContext("2d");

ctx.fillStyle = "purple";

var requestID; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0,0,500,500);
}

var radius = 0;
var growing = "true";

var drawDot = () => {
    clear();
    ctx.beginPath();
    if (radius <= 250) {
        radius += 1
        ctx.arc(250, 250, radius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
        requestAnimationFrame(drawDot)
    }
    else {
        growing = "false";
        cancelAnimationFrame(drawDot)
    }
}

var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);