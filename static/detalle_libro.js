document.addEventListener("DOMContentLoaded", function() {
    const libro = JSON.parse(localStorage.getItem("detalle_libro"));

    if (libro) {
        document.getElementById("detalle-imagen").src = libro.imagenSrc;
        document.getElementById("detalle-titulo").textContent = libro.titulo;
        document.getElementById("detalle-resumen").textContent = libro.resumen;
        document.getElementById("detalle-precio").textContent = "Precio: " + libro.precio;
        document.getElementById("detalle-puntuacion").innerHTML = libro.puntuacion;
    }
});
