from flask import request
from src.drivers.jwt_handler import JwtHandler

def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get('Authorization')
    user_id = request.headers.get('uid')
    if not raw_token or not user_id:
        raise Exception('Invalid auth informations')
    token = raw_token.split()[1]
    token_data = jwt_handler.decode_jwt_token(token)
    token_uid = token_data.get('user_id')
    if isinstance(token_uid, dict):
        token_uid = token_uid.get('user_id')
    if token_uid is not None and user_id and (int(token_uid) == int(user_id)):
        return token_data
    raise Exception('User unauthorized')

