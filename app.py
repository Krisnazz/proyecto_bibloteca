from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('usuarios.db')
    conn.row_factory = sqlite3.Row 
    return conn

def crear_tabla_usuarios():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()


# Datos Libros detalles 

libros = {

1: {
    'titulo': 'La Canción De Aquiles',
    'img': 'img/libro1.jpeg',
    'puntuacion': 5,
    'resumen': 'Grecia en la era de los héroes. Patroclo, un príncipe joven y torpe, ha sido exiliado al reino de Ftía, donde vive a la sombra del rey Peleo y su hijo divino, Aquiles. Aquiles, el mejor de los griegos, es todo lo que no es Patroclo: fuerte, apuesto, hijo de una diosa. Un día Aquiles toma bajo su protección al lastimoso príncipe y ese vínculo provisional da paso a una sólida amistad mientras ambos se convierten en jóvenes habilidosos en las artes de la guerra. Pero el destino nunca está lejos de los talones de Aquiles. Cuando se extiende la noticia del rapto de Helena de Esparta, se convoca a los hombres de Grecia para asediar la ciudad de Troya. Aquiles, seducido por la promesa de un destino glorioso, se une a la causa, y Patroclo, dividido entre el amor y el miedo por su compañero, lo sigue a la guerra. Poco podía imaginar que los años siguientes iban a poner a prueba todo cuanto habían aprendido y todo cuanto valoraban profundamente.',
    'precio': '$7.990',
    'categoria': 'ficcion'

},

2: {
    'titulo': 'Alas De Hierro (2)',
    'img': 'img/libro2.webp',
    'puntuacion': 5,
    'resumen': 'Todos esperaban que Violet Sorrengail muriera en su primer año en el Colegio de Guerra de Basgiath, incluso ella misma. Pero la Trilla fue tan solo la primera de una serie de pruebas imposibles destinadas a deshacerse de los pusilánimes, los indignos y los desafortunados. Ahora comienza el verdadero entrenamiento y Violet no sabe cómo logrará superarlo. No solo porque es brutal y agotador ni porque está diseñado para llevar al límite el umbral del dolor de los jinetes, sino porque el nuevo vicecomandante está empeñado en demostrar a Violet lo débil que es a menos que traicione al hombre que ama.',
    'precio': '$5.990',
    'categoria': 'fantasia'
},

3: {
    'titulo': 'El Principe Cruel',
    'img': 'img/libro3.webp',
    'puntuacion': 5,
    'resumen': 'Jude tenía siete años cuando sus padres fueron asesinados y, junto con sus hermanas, fue trasladada a la traicionera Corte Suprema de Faerie. Diez años más tarde, lo único que Jude desea, a pesar de ser una simple mortal, es sentir que pertenece a ese lugar. Pero la mayoría de los seres feéricos desprecian a los humanos. Especialmente el príncipe Cardan, el hijo más joven y perverso del rey supremo. Para hacerse un hueco en la corte, Jude deberá enfrentarse a él. Y afrontar las consecuencias. Como resultado, se verá envuelta en una red de intrigas entre inmortales, y descubrirá su propia habilidad para el derramamiento de sangre.',
    'precio': '$6.990',
    'categoria': 'fantasia'
},

4: {
    'titulo': 'Indigno De Ser Humano',
    'img': 'img/libro9.jpeg',
    'puntuacion': 5,
    'resumen': 'Repudiado por su familia tras un intento de suicidio e incapaz de vivir en armonía con sus hipócritas semejantes, Yozo malvive como dibujante de historietas y subsiste gracias a la ayuda de mujeres que se enamoran de él pese a su alcoholismo y adicción a la morfina.',
    'precio': '$5.990',
    'categoria': 'ficcion'
    },

5: {
    'titulo': 'Destroza Me',
    'img': 'img/libro4.jpeg',
    'puntuacion': 5,
    'resumen': 'La piel de Juliette es mortal. La última vez que toco a alguien, lo mató. Por eso lleva 264 días encerrada en una celda, sin tocar a nadie. En el exterior, el mundo está devastado: los animales, las plantas y el cielo azul no son más que el cuento de un pasado feliz. Las personas que han sobrevivido solo tienen una palabra en sus mentes: "guerra". Y Warner, un joven perverso, es quien intenta restablecer el orden en medio del caos. pero ¿cuál será el precio a pagar?',
    'precio': '$7.990',
    'categoria': 'ficcion'
    },

6: {
    'titulo': 'Un Cuento Perfecto',
    'img': 'img/libro5.jpeg',
    'puntuacion': 5,
    'resumen': 'Margot es la pequeña de tres hermanas nacidas y educadas en el seno de una familia adinerada y algo rancia. Siempre luchó por ser la princesa de su propio cuento: tiene una carrera de éxito, un sueldazo, un piso en la Castellana y un novio absolutamente perfecto. Pero… el día de su boda sufre un ataque de histeria que provoca que se tenga que suspender la celebración. Margot, destrozada, decide ahogar las penas en una noche loca de alcohol y bailes. Sin embargo… la noche se complica y el día siguiente despierta en su cama con una resaca brutal y junto a un jovencito completamente desnudo. David es un alma libre que va a dedicar todos sus ahorros en dar la vuelta al mundo. Sobre el amor… tiene la misma visión: quiere volar. Es un Casanova moderno que deja a sus amantes con una sonrisa. Un domingo, después de una noche loca, despierta en una gigantesca cama, en un piso enorme, junto a una chica preciosa. Se las ingenia para volver a verla y Margot, aunque está obsesionada con recuperar a su novio y su vida perfecta, decide tener una fugaz aventura con ese joven tan guapo. Nadie lo sabrá, ambos ganan: será divertido, sin compromiso, pasarán un buen rato y en septiembre se dirán adiós sin más. Un viaje a Grecia, una conexión que no esperaban y la intimidad entre dos personas que pertenecen a dos mundos completamente diferentes, sin nada en común, complicará los objetivos de ambos.',
    'precio': '$4.990',
    'categoria': 'romance'
},

7: {
    'titulo': 'La Hija De La Diosa De La Luna',
    'img': 'img/libro8.png',
    'puntuacion': 5,
    'resumen': 'Al crecer en la luna, Xingyin está acostumbrada a la soledad, sin saber que se la está ocultando del temido Emperador Celestial, que exilió a su madre por robar el elixir de la inmortalidad. Pero cuando la magia de Xingyin se manifiesta y su existencia es descubierta, se ve obligada a abandonar su hogar y dejar atrás a su madre. Sola, indefensa y asustada, se abre camino hasta el Reino Celestial, una tierra de ensueño llena de secretos. Tras ocultar su identidad, aprovecha la oportunidad de entrenar junto al hijo del Emperador, exhibiendo dotes maestras para la arquería y la magia, incluso cuando la llama de la pasión se enciende entre el príncipe y ella.',
    'precio': '$6.990',
    'categoria': 'fantasia'
},

8: {
    'titulo': 'Tan Poca Vida',
    'img': 'img/libro10.webp',
    'puntuacion': 5,
    'resumen': 'Tan poca vida, una historia que recorre más de tres décadas de amistad en la vida de cuatro hombres que crecen juntos en Manhattan. Cuatro hombres que tienen que sobrevivir al fracaso y al éxito y que, a lo largo de los años, aprenden a sobreponerse a las crisis económicas, sociales y emocionales. Cuatro hombres que comparten una idea muy peculiar de la intimidad, una manera de estar juntos hecha de pocas palabras y muchos gestos. Cuatro hombres cuya relación la autora utiliza para realizar una minuciosa indagación de los límites de la naturaleza humana.',
    'precio': '$5.990',
    'categoria': 'novela'
},

9: {
    'titulo': 'Al Final Mueren Los Dos',
    'img': 'img/libro13.webp',
    'puntuacion': 5,
    'resumen': ' En un presente alternativo, en el que es posible predecir la muerte con un plazo de veinticuatro horas, Mateo Torrez y Rufus Emeterio acaban de recibir la llamada más temida: la misma que te avisa de que ha llegado tu hora final. En circunstancias normales, es poco probable que Mateo y Rufus se hubieran conocido. Pero sus circunstancias no son normales en absoluto. Porque les quedan, a lo sumo, veinticuatro horas de vida. Y han decidido recurrir a Último Amigo, la aplicación de citas que te permite contactar con alguien dispuesto a compartir tu carga. Mateo y Rufus tienen un día, puede que menos, para disfrutar de su recién nacida amistad. Para descubrir cuán frágiles y preciosos son los hilos que nos unen. Para mostrar al mundo su verdadero yo.',
    'precio': '$5.990',
    'categoria': 'ficcion'
},

10: {
    'titulo': 'Los 7 Maridos De Evelyn Hugo',
    'img': 'img/libro14.webp',
    'puntuacion': 5,
    'resumen': 'Todos esperaban que Violet Sorrengail muriera en su primer año en el Colegio de Guerra de Basgiath, incluso ella misma. Pero la Trilla fue tan solo la primera de una serie de pruebas imposibles destinadas a deshacerse de los pusilánimes, los indignos y los desafortunados. Ahora comienza el verdadero entrenamiento y Violet no sabe cómo logrará superarlo. No solo porque es brutal y agotador ni porque está diseñado para llevar al límite el umbral del dolor de los jinetes, sino porque el nuevo vicecomandante está empeñado en demostrar a Violet lo débil que es a menos que traicione al hombre que ama.',
    'precio': '$6.990',
    'categoria': 'romance'
},

11: {
    'titulo': 'La Bibloteca De La Media Noche',
    'img': 'img/libro15.webp',
    'puntuacion': 5,
    'resumen': '«Entre la vida y la muerte hay una biblioteca. Y los estantes de esa biblioteca son infinitos. Cada libro da la oportunidad de probar otra vida que podrías haber vivido y de comprobar cómo habrían cambiado las cosas si hubieras tomado otras decisiones... ¿Habrías hecho algo de manera diferente si hubieras tenido la oportunidad?». Nora Seed aparece, sin saber cómo, en la Biblioteca de la Medianoche, donde se le ofrece una nueva oportunidad para hacer las cosas bien. Hasta ese momento, su vida ha estado marcada por la infelicidad y el arrepentimiento. Nora siente que ha defraudado a todos, y también a ella misma. Pero esto está a punto de cambiar. Los libros de la Biblioteca de la Medianoche permitirán a Nora vivir como si hubiera hecho las cosas de otra manera. Con la ayuda de una vieja amiga, tendrá la opción de esquivar todo aquello que se arrepiente de haber hecho (o no haber hecho), en pos de la vida perfecta. Pero las cosas no siempre serán como imaginó que serían, y pronto sus decisiones enfrentarán a la Biblioteca y a ella misma en un peligro extremo. Nora deberá responder una última pregunta antes de que el tiempo se agote: ¿cuál es la mejor manera de vivir?',
    'precio': '$5.990',
    'categoria': 'fantasia'
},

12: {
    'titulo': 'El marciano',
    'img': 'img/libro18.webp',
    'puntuacion': 5,
    'resumen': 'Mark Watney, es dado por muerto por su tripulación, en una misión en el planeta Marte, al poco tiempo del despegue de la nave Mark se da cuenta que se ha quedado solo en Marte y tiene que usar todo su ingenio y su entrenamiento para sobrevivir en planeta Marte.',
    'precio': '$5.990',
    'categoria': 'ficcion'
},

13: {
    'titulo': 'Yo, Robot',
    'img': 'img/libro17.webp',
    'puntuacion': 5,
    'resumen': 'En el año 2035, los robots son parte de la vida cotidiana. Cuando la confianza en ellos se rompe, sólo un hombre contra todo el sistema lo ve venir.',
    'precio': '$7.990',
    'categoria': 'ficcion'
},

14: {
    'titulo': 'De sangres y cenizas',
    'img': 'img/libro11.jpg',
    'puntuacion': 5,
    'resumen': 'En el año 2035, los robots son parte de la vida cotidiana. Cuando la confianza en ellos se rompe, sólo un hombre contra todo el sistema lo ve venir.',
    'precio': '$6.990',
    'categoria': 'ficcion'
},

15: {
    'titulo': 'Dune',
    'img': 'img/libro16.webp',
    'puntuacion': 5,
    'resumen': 'Habitado por los monstruosos gusanos de arena de centenares de metros de longitud. Sin embargo, cuando la familia es traicionada, su hijo y heredero, Paul, emprenderá un viaje hacia un destino más grande del que jamás hubiese podido soñar.',
    'precio': '$7.990',
    'categoria': 'ficcion'
},



}


@app.route('/')
def index():
    return render_template('index.html', libros=libros.values())


@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/libro/<int:id>')
def detalle_libro(id):
    libro = libros.get(id)
    if libro:
        libro['img_url'] = url_for('static', filename=libro['img'])
        return render_template('detalle_libro.html', libro=libro)
    else:
        return "Libro no encontrado", 404

@app.route('/registro', methods=['POST'])
def registro():
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)', (nombre, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))  
    except sqlite3.IntegrityError:
        return "Este email ya está registrado", 400
    except Exception as e:
        return str(e), 500


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    usuario = conn.execute('SELECT * FROM usuarios WHERE email = ? AND password = ?', (email, password)).fetchone()
    conn.close()

    if usuario:
        session['usuario_id'] = usuario['id']
        return redirect(url_for('index')) 
    else:
        return "Intenta de nuevo."


@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('query', '').lower()
    if query:
        libros_filtrados = {id: libro for id, libro in libros.items() if query in libro['titulo'].lower() or query in libro['categoria'].lower()}
    else:
        libros_filtrados = libros

    return jsonify(libros_filtrados)


if __name__ == '__main__':
    crear_tabla_usuarios()  
    app.run(debug=True)

