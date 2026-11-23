class MultimodalMemoryEngine:

    def __init__(self):

        self.text_memories = []
        self.image_memories = []
        self.audio_memories = []

    def store_text(
        self,
        text
    ):

        self.text_memories.append(
            text
        )

    def store_image(
        self,
        image
    ):

        self.image_memories.append(
            image
        )

    def store_audio(
        self,
        audio
    ):

        self.audio_memories.append(
            audio
        )

    def retrieve_all(self):

        return {

            "text":
            self.text_memories,

            "images":
            self.image_memories,

            "audio":
            self.audio_memories
        }
      
