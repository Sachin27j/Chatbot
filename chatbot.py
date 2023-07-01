import openai
from dotenv import dotenv_values
import argparse

def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end
 
 
def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end
 
def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end


def main():    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--personality",type=str,help="A brief summary of chatbot's personality",default="friendly and helpful chatbot")
    personality = parser.parse_args().personality
    print(personality)
    config = dotenv_values(".env")
    openai.api_key =config["OpenAIKey"]
    messages=[{"role":"system","content":f"You are a chatbot whose mood is : {personality}"}]
    while True:
        try:
            userInput = input(bold(blue("You: ")))
            messages.append({"role":"user","content":userInput})
            response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages,
            max_tokens=200
            )
            messages.append(response.choices[0].message.to_dict())
            print(bold(red("Assistant: ")),response.choices[0].message.content)
        except KeyboardInterrupt:
            val = bold(red("Assistant"))
            print(f"\n {val}: Bye Bye")
            break
if __name__ == '__main__':
    main()