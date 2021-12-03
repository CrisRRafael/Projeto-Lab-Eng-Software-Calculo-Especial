from flask_cors import CORS
from flask import request, Response,Flask, jsonify
from controller_calc_esp import CalcEspController
import json

app = Flask(__name__)
CORS(app)


@app.route('/calc_raiz', methods=["GET"])
def create():
    print('aqui')
    str_raiz = request.args.get('str_input')
    resultado = CalcEspController.calcular_raiz(str_raiz)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)