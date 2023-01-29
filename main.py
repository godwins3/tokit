import openai

openai.api_key = "YOUR_API_KEY"

def fetch_response(prompt):
  completions = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message

user_input = input("Ask a question: ")
response = fetch_response(user_input)
print("ChatGPT: ", response)
