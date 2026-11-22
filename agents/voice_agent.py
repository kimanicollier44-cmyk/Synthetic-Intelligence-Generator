class VoiceAgent:

    def __init__(
        self,
        speech_to_text,
        text_to_speech
    ):

        self.stt = speech_to_text
        self.tts = text_to_speech

    def transcribe(
        self,
        audio_file
    ):

        return self.stt.process(
            audio_file
        )

    def speak(
        self,
        text,
        output_file
    ):

        self.tts.generate(
            text,
            output_file
        )

        return output_file
      
