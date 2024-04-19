var canvas, ctx;
        
        function draw() {
            canvas = document.getElementById('bingo-canvas');
            ctx = canvas.getContext('2d');

            // Cargar la imagen del cartón del bingo
            var img = new Image();
            img.onload = function() {
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
            };
            img.src = "{{ bingo_card.image.url }}";

            // Manejar el clic del usuario en el canvas
            canvas.addEventListener('mousedown', function(e) {
                drawCircle(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
            });
        }

        function drawCircle(x, y) {
            ctx.beginPath();
            ctx.arc(x, y, 5, 0, Math.PI * 2);
            ctx.fillStyle = 'red';
            ctx.fill();
            ctx.closePath();
        }