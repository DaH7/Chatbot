import ollama

desiredModel = 'deepseek-r1:14b'

question = 'How do i run my code in visual studio without pressing the run button'
response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'user',
        'content': question,

    }
])

OllamaResponse = response['message']['content']

print(OllamaResponse)

# with open("OutputOllama.txt","w", encoding="utf-8") as text_file:
#    text_file.write(OllamaResponse)
