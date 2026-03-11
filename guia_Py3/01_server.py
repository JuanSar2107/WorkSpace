from flask import Flask 
app = Flask(__name__) 

@app.route('/', methods=['GET']) # 
def home() -> str:
    return "<h1>Sistema de Control Agroindustrial Activo</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)