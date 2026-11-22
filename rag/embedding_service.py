import hashlib


class EmbeddingService:

    def create_embedding(
        self,
        text
    ):

        digest = hashlib.sha256(
            text.encode()
        ).hexdigest()

        values = []

        for i in range(0, 64, 4):

            chunk = digest[i:i+4]

            values.append(
                int(chunk, 16)
            )

        return values
      
