document.addEventListener("DOMContentLoaded", function() {

// Carrusel Principal

    const carrusel = document.querySelector(".carrusel");
    const carruselItems = document.querySelectorAll(".carrusel_item");
    const prevBtnCarrusel = document.querySelector(".carrusel_btn.prev");
    const nextBtnCarrusel = document.querySelector(".carrusel_btn.next");
    const indicadores = document.querySelectorAll(".indicador");
    let currentIndexCarrusel = 0;

    function updateCarrusel() {
        carrusel.style.transform = `translateX(-${currentIndexCarrusel * 50}%)`;
        indicadores.forEach((indicador, index) => {
            indicador.classList.toggle('active', index === currentIndexCarrusel);
        });
    }

    function showNextItemCarrusel() {
        currentIndexCarrusel = (currentIndexCarrusel + 1) % carruselItems.length;
        updateCarrusel();
    }

    function showPrevItemCarrusel() {
        currentIndexCarrusel = (currentIndexCarrusel - 1 + carruselItems.length) % carruselItems.length;
        updateCarrusel();
    }

    nextBtnCarrusel.addEventListener("click", showNextItemCarrusel);
    prevBtnCarrusel.addEventListener("click", showPrevItemCarrusel);

    indicadores.forEach((indicador, index) => {
        indicador.addEventListener("click", () => {
            currentIndexCarrusel = index;
            updateCarrusel();
        });
    });

    setInterval(showNextItemCarrusel, 10000); 

// Destacados

    const destacadosCarrusel = document.querySelector(".destacados");
    const destacadosItems = document.querySelectorAll(".destacados_item");
    const prevBtnDestacados = document.querySelector(".destacados_btn.prev");
    const nextBtnDestacados = document.querySelector(".destacados_btn.next");
    let currentIndexDestacados = 0;

    function updateDestacados() {
        destacadosCarrusel.style.transform = `translateX(-${currentIndexDestacados * 100}%)`;
    }

    function showNextItemDestacados() {
        currentIndexDestacados = (currentIndexDestacados + 1) % destacadosItems.length;
        updateDestacados();
    }

    function showPrevItemDestacados() {
        currentIndexDestacados = (currentIndexDestacados - 1 + destacadosItems.length) % destacadosItems.length;
        updateDestacados();
    }

    nextBtnDestacados.addEventListener("click", showNextItemDestacados);
    prevBtnDestacados.addEventListener("click", showPrevItemDestacados);

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

// clic en el icono del usuario

        document.getElementById("openModal").addEventListener("click", function() {
            document.getElementById("modalRegistro").style.display = "flex";
        });

// Cerrar al hacer clic fuera del contenido

        window.onclick = function(event) {
            if (event.target == document.getElementById("modalRegistro")) {
                document.getElementById("modalRegistro").style.display = "none";
            }
        };

});
