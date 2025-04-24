import speech_recognition as sr
import pyttsx3
import webbrowser
import openai  # Import the whole openai module

import os
import time

engine = pyttsx3.init()


def talk(words):
    """
    Make the assistant say the given words.

    Args:
        words (str): The words to be spoken by the assistant.
    """
    try:
        engine.say(words)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")


def ai_command(command):
    api_key = os.getenv("OPENAI_API_KEY")
    # Use openai.OpenAI instead of OpenAI
    client = openai.OpenAI(api_key=api_key)
    max_retries = 5
    delay = 5

    for attempt in range(max_retries):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "You are a virtual assistant named Kitty."},
                          {"role": "user", "content": command}]
            )
            return completion.choices[0].message.content
        except openai.RateLimitError:  # Now openai.RateLimitError works
            print(f"Rate limit exceeded. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2
        except openai.OpenAIError as e:
            print(f"OpenAI API Error: {e}")
            break
    return "Unable to get a response due to API limits."


def process_command(command):
    print("Command received:", command)
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.co.in")
        talk("Opening Google")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            talk(f"Searching Google for {query}")
        else:
            talk("Please specify what to search for.")
    else:
        # Using OpenAI's GPT-3 to generate a response
        output = ai_command(command)
        talk(output)


def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # talk("Please say Hello Kitty to activate me.")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            command = r.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    return None


if __name__ == "__main__":
    talk("Initializing Kitty")

    while True:
        word = listen_for_command()
        if word and word.lower() == "hello kitty":
            print("Kitty Active, please speak...")
            process_command(word)
            # if command:
            #     process_command(command)
        else:
            talk("I am sorry, I did not understand what you said.")
