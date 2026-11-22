from models.gemini.client import GeminiClient
from orchestration.flowx.router import Router

def main():
    model = GeminiClient()
    router = Router(model)

    while True:
        user_input = input("> ")
        result = router.process(user_input)
        print(result)

if __name__ == "__main__":
    main()
