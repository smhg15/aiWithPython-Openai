import openai as op

#this code work with 'text-davinci-003' engine.

op.api_key = 'YOUR_API_KEY' #you have to take it from your openai account

# insert the code in a while loop for make some questions
while True:
    prompt = input('\nHow can i help you?: ')

    if prompt == 'quit':
        break

    completion = op.Completion.create(engine='text-davinci-003', #Last engine, when i code this is gpt-3.5-turbo but not work. Return this error: 'openai.error.InvalidRequestError: This is a chat model and not supported in the v1/completions endpoint'
                                  prompt = prompt, #define the initial prompt
                                  n = 1, #with the value: 1, you can skip this line and work too
                                  max_tokens= 2048) #max value with this engine:4096
    
    print(completion.choices[0].text)
