from ollama import chat

# setting up
response = chat(
    model='deepseek-r1',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)