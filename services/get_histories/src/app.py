'''Archivo que ejecuta la aplicacion'''
from flask import request

from config.config import server_config
from config.config import get_app
from config.config import run_app
from endpoint.get_histories import GetHistories

app = get_app(__name__)
server_config(app)

@app.route('/histories')
def get_histories():
    get_histories = GetHistories()
    return get_histories(request)
    # return jsonify({"msg": "Tu... si tu el que lee esto, debes saber que me costo desplegar esta vaina asi que valorala xd"})

if __name__ == '__main__':
    run_app(app)
