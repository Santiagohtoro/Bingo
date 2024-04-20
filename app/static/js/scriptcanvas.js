var canvas, ctx;
var imgn =document.querySelector(".numberTab");

function draw() {
    canvas = document.getElementById('bingo-canvas');
    ctx = canvas.getContext('2d');
    number = imgn.textContent;
    
    var img = new Image();
    img.onload = function () {
        
        ctx.drawImage(img, 0, 0, 500, 800);
    };
    img.src = "../static/img/Tarjetas/" + number + ".png";


    
    canvas.addEventListener('mousedown', function (e) {
        drawCircle(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    });
}

function drawCircle(x, y) {
    ctx.beginPath();
    ctx.arc(x, y, 35, 0, Math.PI * 2);
    ctx.fillStyle = `rgb(166, 100, 229, 0.6)`;
    ctx.fill();
    ctx.closePath();
}

draw(imgn);