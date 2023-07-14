from gpt4all import GPT4All
#model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
#output = model.generate("The capital of France is ", max_tokens=3)
#print(output)


model = GPT4All(model_name='orca-mini-3b.ggmlv3.q4_0.bin')
with model.chat_session():
    response = model.generate(prompt='hello', top_k=1)
    response = model.generate(prompt='write me a short poem', top_k=1)
    response = model.generate(prompt='thank you', top_k=1)
    print(model.current_chat_session)