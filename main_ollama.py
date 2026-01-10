import ollama

def play_game():
    # Initialize the game state and system prompt
    messages = [
        {
            'role': 'system',
            'content': (
                "You are a Dungeon Master for a text-based adventure game. "
                "Keep descriptions vivid but concise (3-4 sentences). "
                "Always end your response by asking the player: 'What do you do?' "
                "If the player dies, describe the death and say 'GAME OVER'."
            )
        },
        {
            'role': 'assistant',
            'content': "You wake up in a damp, stone cell. A single torch flickers on the wall, and the heavy iron door is slightly ajar. What do you do?"
        }
    ]

    print("--- AI ADVENTURE GAME (Type 'quit' to exit) ---")
    print(f"\nDM: {messages[1]['content']}")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ['quit', 'exit']:
            print("Thanks for playing!")
            break

        # Add player choice to history
        messages.append({'role': 'user', 'content': user_input})

        try:
            # Call Ollama
            response = ollama.chat(model='llama3', messages=messages)
            
            # Get the AI's response
            dm_response = response['message']['content']
            print(f"\nDM: {dm_response}")

            # Keep the history updated
            messages.append({'role': 'assistant', 'content': dm_response})

        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            break

if __name__ == "__main__":
    play_game()