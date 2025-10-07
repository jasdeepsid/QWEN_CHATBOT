import ollama


def chat_with_qwen():
    # Simple chat bot with Qwen
    """This is a multi
    -line comment."""
    print("Quen 2 Chatbot (type 'quit' to exit)")
    print("-" * 50)

    conversation_history = []

    while True:
        # capture user input
        user_input = input("\n You:").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        if not user_input:
            continue

        # add user input to message history
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # response from the Qwen model
            response = ollama.chat(
                model="qwen2:0.5b",
                messages=conversation_history,
                max_tokens=512,
                temperature=0.7,
            )

            assistant_message = response['message']['content']

            #add assistant response to message history
            conversation_history.append({"role": "assistant", "content": assistant_message})

            print(f"\n Qwen: {assistant_message}")
            
        except Exception as e:
            print(f"Error: {e}")
