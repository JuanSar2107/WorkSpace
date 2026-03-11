from flask import Flask

app = Flask(__name__)

@app.route('/api/saludar/<string:nombre>', methods=['GET'])
def saludar(nombre: str) -> str:
    return f"Hola {nombre}, tu solicitud fue enrutada exitosamente."

@app.route('/api/temperatura/<float:grados_c>', methods=['GET'])
def convertir_temperatura(grados_c: float) -> str:
    fahrenheit = (grados_c * 9/5) + 32
    return f"Resultado: {grados_c}°C equivalen a {fahrenheit:.2f}°F"

if __name__ == '__main__':
    app.run(debug=True)