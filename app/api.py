from fastapi import FastAPI

from models.gemini.client import GeminiClient
from orchestration.flowx.router import Router


app = FastAPI(
    title="Synthetic Intelligence Generator"
)

model = GeminiClient()

router = Router(model)


@app.get("/")
def health():

    return {
        "status": "online"
    }


@app.post("/generate")
def generate(
    request: dict
):

    prompt = request.get(
        "prompt",
        ""
    )

    response = router.process(
        prompt
    )

    return {
        "response": response
    }
  
