
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/calc_raiz')

def calcular_raiz():
   valores = request.args.get('str_input')
   indice= float(valores[0])
   radicando = float(valores[1])
   resultado = radicando **(1/indice)
   str_output = {'resultado': resultado}
   return jsonify(str_output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)


