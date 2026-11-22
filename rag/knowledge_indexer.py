class KnowledgeIndexer:

    def __init__(
        self,
        vector_store,
        embedding_service
    ):

        self.store = vector_store

        self.embeddings = (
            embedding_service
        )

    def index_document(
        self,
        document_text
    ):

        vector = (
            self.embeddings
            .create_embedding(
                document_text
            )
        )

        self.store.save_memory({

            "text":
            document_text,

            "embedding":
            vector
        })

        return True
      
