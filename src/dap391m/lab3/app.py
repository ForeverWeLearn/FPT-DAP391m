import lmstudio as lms


def main():
    model = lms.llm("google/gemma-4-e2b")

    chat = lms.Chat("You are a helpful and concise local AI assistant.")

    while True:
        user_input = input("\033[32m> \033[0m")
        if user_input.lower() in ["quit", "exit"]:
            break

        if not user_input.strip():
            continue

        chat.add_user_message(user_input)

        print("\n", end="", flush=True)

        for fragment in model.respond_stream(chat, on_message=chat.append):
            print(fragment.content, end="", flush=True)

        print("\n")
