from flask import Flask, render_template, url_for

app = Flask(__name__)

# Datos Libros detalles 

libros = {
    1: {
        'titulo': 'La Canción De Aquiles',
        'img': 'img/libro1.jpeg',
        'puntuacion': 5,
        'resumen': 'Grecia en la era de los héroes. Patroclo, un príncipe joven y torpe, ha sido exiliado al reino de Ftía, donde vive a la sombra del rey Peleo y su hijo divino, Aquiles. Aquiles, el mejor de los griegos, es todo lo que no es Patroclo: fuerte, apuesto, hijo de una diosa. Un día Aquiles toma bajo su protección al lastimoso príncipe y ese vínculo provisional da paso a una sólida amistad mientras ambos se convierten en jóvenes habilidosos en las artes de la guerra. Pero el destino nunca está lejos de los talones de Aquiles. Cuando se extiende la noticia del rapto de Helena de Esparta, se convoca a los hombres de Grecia para asediar la ciudad de Troya. Aquiles, seducido por la promesa de un destino glorioso, se une a la causa, y Patroclo, dividido entre el amor y el miedo por su compañero, lo sigue a la guerra. Poco podía imaginar que los años siguientes iban a poner a prueba todo cuanto habían aprendido y todo cuanto valoraban profundamente.',
        'precio': '$7.990'
    },

    2: {
        'titulo': 'Alas De Hierro (2)',
        'img': 'img/libro2.webp',
        'puntuacion': 4,
        'resumen': 'Todos esperaban que Violet Sorrengail muriera en su primer año en el Colegio de Guerra de Basgiath, incluso ella misma. Pero la Trilla fue tan solo la primera de una serie de pruebas imposibles destinadas a deshacerse de los pusilánimes, los indignos y los desafortunados. Ahora comienza el verdadero entrenamiento y Violet no sabe cómo logrará superarlo. No solo porque es brutal y agotador ni porque está diseñado para llevar al límite el umbral del dolor de los jinetes, sino porque el nuevo vicecomandante está empeñado en demostrar a Violet lo débil que es a menos que traicione al hombre que ama.',
        'precio': '$5.990'
    }
}

@app.route('/')
def index():
    return render_template('index.html', libros=libros.values())

@app.route('/libro/<int:id>')
def detalle_libro(id):
    libro = libros.get(id)
    if libro:
        libro['img_url'] = url_for('static', filename=libro['img'])
        return render_template('detalle_libro.html', libro=libro)
    else:
        return "Libro no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
