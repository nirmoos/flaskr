# from flask.views import MethodView
# from flask import jsonify, current_app as app


# class UserAPI(MethodView):
#     def get(self):
#         return jsonify({'id': '1234'})
#
#
# user_view = UserAPI.as_view('user_api')
# app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET',])
# app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
# app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

from . import user
from flask import jsonify


@user.route('/', methods=['GET'])
def test_url():
    return jsonify({'id': '007'})