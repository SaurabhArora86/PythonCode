import openai  # Import the whole openai module

import os
import time

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)  # Use openai.OpenAI instead of OpenAI


def get_response():
    max_retries = 5
    delay = 5

    for attempt in range(max_retries):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "You are a virtual assistant named Kitty."},
                          {"role": "user", "content": "What is coding?"}]
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


response = get_response()
print(response)
