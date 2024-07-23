document.addEventListener('DOMContentLoaded', () => {
    // Datos de ejemplo para el carrusel y destacados
    const librosCarrusel = [
        { imagen: 'libro1.jpg', titulo: 'Libro 1', resumen: 'Resumen del libro 1', puntuacion: '⭐⭐⭐⭐', precio: '$10' },
        { imagen: 'libro2.jpg', titulo: 'Libro 2', resumen: 'Resumen del libro 2', puntuacion: '⭐⭐⭐⭐⭐', precio: '$15' },
    ];

    const librosDestacados = [
        { imagen: 'libro3.jpg', titulo: 'Libro 3', resumen: 'Resumen del libro 3', puntuacion: '⭐⭐⭐⭐⭐', precio: '$20' },
        { imagen: 'libro4.jpg', titulo: 'Libro 4', resumen: 'Resumen del libro 4', puntuacion: '⭐⭐⭐⭐', precio: '$12' },
    ];

    // crear un libro
    function crearLibro(libro, esDestacado = false) {
        const item = document.createElement('div');
        item.classList.add(esDestacado ? 'destacados_item' : 'carrusel_item');

        item.innerHTML = `
            <img src="${libro.imagen}" alt="${libro.titulo}">
            <div class="${esDestacado ? 'destacados_detalles' : 'carrusel_detalles'}">
                <div class="${esDestacado ? 'libro_titulo_destacado' : 'libro_titulo'}">${libro.titulo}</div>
                <div class="${esDestacado ? 'libro_resumen_destacado' : 'libro_resumen'}">${libro.resumen}</div>
                <div class="${esDestacado ? 'libro_puntuacion_destacado' : 'libro_puntuacion'}">${libro.puntuacion}</div>
                <div class="${esDestacado ? 'libro_precio_destacado' : 'libro_precio'}">${libro.precio}</div>
                <button class="${esDestacado ? 'btn_comprar_destacado' : 'btn_comprar'}">Comprar</button>
                <button class="${esDestacado ? 'btn_guardar_destacado' : 'btn_guardar'}"><img src="icono_guardar.png" alt="Guardar"></button>
            </div>
        `;

        return item;
    }

    // Agregar libros al carrusel
    const carrusel = document.querySelector('.carrusel');
    librosCarrusel.forEach(libro => {
        const libroElement = crearLibro(libro);
        carrusel.appendChild(libroElement);
    });

    // Agregar libros destacados
    const destacadosContainer = document.querySelector('.destacados');
    librosDestacados.forEach(libro => {
        const libroElement = crearLibro(libro, true);
        destacadosContainer.appendChild(libroElement);
    });

    // Funciones de navegación del carrusel
    const prevBtnCarrusel = document.querySelector('.carrusel_btn.prev');
    const nextBtnCarrusel = document.querySelector('.carrusel_btn.next');
    let indexCarrusel = 0;

    function mostrarCarrusel() {
        const items = document.querySelectorAll('.carrusel_item');
        const totalItems = items.length;

        if (indexCarrusel < 0) {
            indexCarrusel = totalItems - 1;
        } else if (indexCarrusel >= totalItems) {
            indexCarrusel = 0;
        }

        const offset = -indexCarrusel * 100;
        document.querySelector('.carrusel').style.transform = `translateX(${offset}%)`;
    }

    prevBtnCarrusel.addEventListener('click', () => {
        indexCarrusel--;
        mostrarCarrusel();
    });

    nextBtnCarrusel.addEventListener('click', () => {
        indexCarrusel++;
        mostrarCarrusel();
    });

    // Funcione navegación 
    const prevBtnDestacados = document.querySelector('.destacados_btn.prev');
    const nextBtnDestacados = document.querySelector('.destacados_btn.next');
    let indexDestacados = 0;

    function mostrarDestacados() {
        const items = document.querySelectorAll('.destacados_item');
        const totalItems = items.length;

        if (indexDestacados < 0) {
            indexDestacados = totalItems - 1;
        } else if (indexDestacados >= totalItems) {
            indexDestacados = 0;
        }

        const offset = -indexDestacados * 100;
        document.querySelector('.destacados').style.transform = `translateX(${offset}%)`;
    }

    prevBtnDestacados.addEventListener('click', () => {
        indexDestacados--;
        mostrarDestacados();
    });

    nextBtnDestacados.addEventListener('click', () => {
        indexDestacados++;
        mostrarDestacados();
    });

    mostrarCarrusel();
    mostrarDestacados();
});
