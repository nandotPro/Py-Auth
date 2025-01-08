import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=jwt_infos["expiration_time"]),
                **body
            },
            key=jwt_infos["secret_key"],
            algorithm=jwt_infos["algorithm"]
        )
        return token
    
    def decode_jwt_token(self, token: str) -> dict:
        token_data = jwt.decode(
            token, jwt_infos["secret_key"], 
            algorithms=jwt_infos["algorithm"]
        )
        return token_data
