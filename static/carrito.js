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

// Menú desplegable de categorías

    const menuBtn = document.getElementById('menu-btn');
    const menuDesplegable = document.getElementById('menu_desplegable');

    menuBtn.addEventListener('click', function() {
        menuDesplegable.classList.toggle('show');
        menuDesplegable.classList.toggle('hidden');
    });

// actualizar el total del carrito

    function actualizarTotalCarrito() {
        let total = 0;
        const precios = document.querySelectorAll('.carrito_precio'); 

        precios.forEach(precio => {
            const valorNumerico = parseFloat(precio.textContent.replace('$', '').replace('.', ''));
            total += isNaN(valorNumerico) ? 0 : valorNumerico; 
        });

        const totalFormateado = `$${total.toLocaleString('es-ES')}`;
        document.querySelector('.total_precio').textContent = totalFormateado; 
    }

// botones de eliminar

    function initDeleteButtons() {
        const deleteButtons = document.querySelectorAll('.carrito_basura'); 

        deleteButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                const item = this.closest('.carrito_item'); 
                const precioElemento = item.querySelector('.carrito_precio').textContent;
                const valorNumerico = parseFloat(precioElemento.replace('$', '').replace('.', ''));

                let totalActual = parseFloat(document.querySelector('.total_precio').textContent.replace('$', '').replace('.', ''));
                totalActual -= isNaN(valorNumerico) ? 0 : valorNumerico;

                const totalFormateado = `$${totalActual.toLocaleString('es-ES')}`;
                document.querySelector('.total_precio').textContent = totalFormateado;

                item.remove();

                actualizarTotalCarrito();

            });
        });
    }

    initDeleteButtons();

    actualizarTotalCarrito();
});
