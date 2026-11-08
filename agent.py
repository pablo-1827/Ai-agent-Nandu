import sys


class AIAgent:
    def respond(self, prompt: str) -> str:
        normalized = prompt.strip().lower()
        if not normalized:
            return "Please provide a prompt."
        if "hello" in normalized or "hi" in normalized:
            return "Hello! How can I help you today?"
        if "help" in normalized:
            return "I can respond to greetings and simple prompts."
        return f"I received: {prompt.strip()}"


def main() -> None:
    prompt = " ".join(sys.argv[1:])
    agent = AIAgent()
    print(agent.respond(prompt))


if __name__ == "__main__":
    main()
