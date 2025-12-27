from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)