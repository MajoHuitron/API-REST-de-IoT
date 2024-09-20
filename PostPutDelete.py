from flask import Flask, request

app = Flask(__name__)

# Ruta para manejar GET, POST, PUT y DELETE
@app.route('/saludo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo():
    if request.method == 'GET':
        return "¡Hola, bienvenido a la API!"
    elif request.method == 'POST':
        return "¡Has enviado una solicitud POST!"
    elif request.method == 'PUT':
        return "¡Has enviado una solicitud PUT para actualizar algo!"
    elif request.method == 'DELETE':
        return "¡Has enviado una solicitud DELETE para eliminar algo!"
    else:
        return "Método no soportado", 405

if __name__ == '__main__':
    app.run(debug=True)
