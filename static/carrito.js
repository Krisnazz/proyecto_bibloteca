document.addEventListener("DOMContentLoaded", function() {

// Manejo de clic en los libros

        document.querySelectorAll(".carrusel_item").forEach(item => {
            item.addEventListener("click", function() {
                const titulo = this.querySelector(".libro_titulo").textContent;
                const resumen = this.querySelector(".libro_resumen") ? this.querySelector(".libro_resumen").textContent : '';
                const puntuacion = this.querySelector(".libro_puntuacion").innerHTML;
                const precio = this.querySelector(".libro_precio").textContent;
                const imagenSrc = this.querySelector("img").src;
        
                localStorage.setItem("detalle_libro", JSON.stringify({
                    titulo,
                    resumen,
                    puntuacion,
                    precio,
                    imagenSrc
                }));
                window.location.href = "detalle_libro.html";
            });
        });

// Menu desplegable de categorías 

        const menuBtn = document.getElementById('menu-btn');
        const menuDesplegable = document.getElementById('menu_desplegable');
    
        menuBtn.addEventListener('click', function() {
            menuDesplegable.classList.toggle('show');
            menuDesplegable.classList.toggle('hidden');
            });
    });
