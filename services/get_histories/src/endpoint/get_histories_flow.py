from models.history import History
from flask import jsonify


class GetHistoriesFlow:

    def __call__(self):
        histories_list = History.objects()

        if len(histories_list) > 0:
            users_jsons_list = []
            users_jsons_list = list(map(lambda history_obj: history_obj.to_json(), histories_list))
            return jsonify({"histories": users_jsons_list})
        return jsonify({"msg": "No hay historias"})
