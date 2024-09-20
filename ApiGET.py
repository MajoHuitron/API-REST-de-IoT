from flask import Flask

app = Flask(__name__)

# Ruta para el método GET que devuelve un saludo
@app.route('/saludo', methods=['GET'])
def saludo():
    return "¡Hola, bienvenido a la API!"

if __name__ == '__main__':
    app.run(debug=True)
