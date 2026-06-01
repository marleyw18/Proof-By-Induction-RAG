from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Prompt for AI model
with open('rubric_prompt', "r") as file:
    rubric = file.read()
    print("...Rubric loaded")

#rubric_prompt = ChatPromptTemplate.from_template("Grade this {proof} using this rubric: " + rubric)

# Define system roles and human inputs using tuples
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an impartial discrete mathematics professors and {rubric}"),
    ("human", "Can I have concise feedback and scoring on the following proof: {proof}"),
])

# initialize the model
model = ChatOllama(model="llama3.1", temperature=.4)

# create the chain (going back and forth with the model)
chain = chat_template | model

# conversation history
history = {}

print('Hi! I am your proof by induction tutor! Ask away. \n')

def chat():
    while True:
        full_response = ""
        message = input('\nYour proof: ')
        # Invoke the template to get a formatted ChatPromptValue
        for result in chain.stream({"rubric": rubric, "proof": message}):
            print(result.content, end="", flush=True)
            # store the full response as it is created
            full_response += result.content

        # add to conversation history
        history[message] = full_response


chat()



