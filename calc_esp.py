
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/calc_raiz')

def calcular_raiz():
   data = request.args.get('str_input')
   valores=data.split(',')
   print(valores)
   indice= int(valores[0])
   radicando = int(valores[1])
   resultado = float(radicando **(1/indice))
   str_raiz = {'resultado': resultado}
   print(str_raiz)   
   return jsonify(str_raiz)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)


