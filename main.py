from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# System rubric_prompt
with open('Prompts/system_prompt', "r") as file:
    prompt = file.read()
    print("...System prompt loaded")

system_prompt = ChatPromptTemplate.from_template(prompt + '{user_message}')

# initialize the model
model = ChatOllama(model="llama3.1")

# create the chain (going back and forth with the model)
chain = system_prompt | model

# conversation history
history = {}

print('Hi! I am your proof by induction tutor! Ask away. \n')
def chat():
    while True:
        user_message = input("\nYou: ")
        if user_message.lower() == 'exit':
            print('Goodbye')
            break
        else:
            print("\nTutor: ", end="", flush=True)
            full_response = ""

            # print text as it renders
            for result in chain.stream({'user_message': user_message}):
                print(result.content, end="", flush=True)

                # store the full response as it is created
                full_response += result.content

                # add to conversation history
                history[user_message] = full_response


if __name__ == "__main__":
    chat()