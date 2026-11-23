class WorldModel:

    def __init__(self):

        self.entities = {}

    def register(
        self,
        entity_id,
        state
    ):

        self.entities[
            entity_id
        ] = state

    def update(
        self,
        entity_id,
        state
    ):

        self.entities[
            entity_id
        ] = state

    def get(
        self,
        entity_id
    ):

        return self.entities.get(
            entity_id
        )

    def snapshot(self):

        return dict(
            self.entities
        )
      
