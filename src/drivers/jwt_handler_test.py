from src.drivers.jwt_handler import JwtHandler

def test_jwt_handler():
    jwt_handler = JwtHandler()
    body = {
        "username": "John Doe",
        "password": "123456"
    }
    token = jwt_handler.create_jwt_token(body)
    token_data = jwt_handler.decode_jwt_token(token)
    assert token is not None
    assert isinstance(token, str)
    assert token_data["username"] == body["username"]
    assert token_data["password"] == body["password"]


