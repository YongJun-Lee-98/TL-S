import os
import openai
import json
import requests

with open('config.json') as f:
    config = json.load(f)

openai.api_key = config["api_key"]
n = 3  # Set the desired number of images to save

prompt = input("Enter the prompt: ")  # Prompt input from the user

response = openai.Image.create(
  prompt=prompt,  # Use the user input as the prompt
  n=n,
  size="1024x1024"
)
print(response)
for i in range(n):
    url = response["data"][i]["url"]
    image_data = requests.get(url).content

    with open(f"image{i+1}.png", "wb") as f:
        f.write(image_data)
