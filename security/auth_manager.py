import os
import jwt
from datetime import datetime, timedelta


class AuthManager:

    def __init__(self):

        self.secret = os.getenv(
            "JWT_SECRET",
            "change-me"
        )

    def create_token(
        self,
        user_id
    ):

        payload = {

            "user_id": user_id,

            "exp":
            datetime.utcnow() +
            timedelta(hours=24)
        }

        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    def verify_token(
        self,
        token
    ):

        try:

            return jwt.decode(
                token,
                self.secret,
                algorithms=["HS256"]
            )

        except Exception:

            return None
          
