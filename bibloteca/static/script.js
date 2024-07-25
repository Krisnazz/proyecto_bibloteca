document.addEventListener("DOMContentLoaded", function() {
    // Carrusel Principal
    const carrusel = document.querySelector(".carrusel");
    const carruselItems = document.querySelectorAll(".carrusel_item");
    const prevBtnCarrusel = document.querySelector(".carrusel_btn.prev");
    const nextBtnCarrusel = document.querySelector(".carrusel_btn.next");
    const indicadores = document.querySelectorAll(".indicador");
    let currentIndexCarrusel = 0;

    function updateCarrusel() {
        carrusel.style.transform = `translateX(-${currentIndexCarrusel * 100}%)`;
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

    setInterval(showNextItemCarrusel, 8000); 

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
});
