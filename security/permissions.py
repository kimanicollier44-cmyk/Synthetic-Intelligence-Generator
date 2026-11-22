class PermissionManager:

    def __init__(self):

        self.roles = {

            "admin": [
                "read",
                "write",
                "delete"
            ],

            "user": [
                "read",
                "write"
            ],

            "guest": [
                "read"
            ]
        }

    def allowed(
        self,
        role,
        action
    ):

        return (
            action in
            self.roles.get(role, [])
        )
      
