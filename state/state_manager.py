class StateManager:

    def __init__(self):

        self.state = {}

    def set(
        self,
        key,
        value
    ):

        self.state[key] = value

    def get(
        self,
        key,
        default=None
    ):

        return self.state.get(
            key,
            default
        )

    def delete(
        self,
        key
    ):

        if key in self.state:

            del self.state[key]

    def snapshot(self):

        return dict(
            self.state
        )
