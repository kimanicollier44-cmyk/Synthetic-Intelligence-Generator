import os

class Config:

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY",
        ""
    )

    APP_NAME = "Synthetic Intelligence Generator"

    MEMORY_PATH = "data/memory"

    OUTPUT_PATH = "outputs"

    LOG_LEVEL = "INFO"
