from flask import jsonify, request
from app.api_1_0.api_exception import ApiException
from app.models import Player
from . import api

@api.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get_or_404(player_id)
    return jsonify(player.to_dict())

@api.route('/players', methods=['GET'])
def get_player_by_token():
    token = request.args.get('token')
    if token is None:
        raise ApiException("Must provide ?token=[player's token] to search for a player")
    player = Player.query.filter_by(token=token).first_or_404()
    return jsonify(player.to_dict())
