class ContextBuilder:

    def __init__(self):
        pass

    def build(
        self,
        user_message,
        memories=None
    ):

        memories = memories or []

        memory_text = "\n".join(memories)

        return f"""
        User Request:
        {user_message}

        Relevant Memory:
        {memory_text}

        Generate best response.
        """
