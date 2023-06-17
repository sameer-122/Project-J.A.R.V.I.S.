import os
import json
import openai
from config import openAi_api_key

openai.api_key = openAi_api_key                           # use -> openai.api_key = os.getenv(OPENAI_API_KEY), if env_var set
def ai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,               #"write a code to play music in system in python.\n",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    s = '*'*100
    print(s, end='')
    print(response['choices'][0]['text'])
    text = response['choices'][0]['text']
    with open(f'Openai/{prompt}', 'w') as f:
        f.write(text)

if __name__ == "__main__":
    prompt = 'write a program to open any stackoverflow in python'
    ai(prompt)


    # q = 'using a i write an email to my boss for resignation'
    # lis = q.split('using a r ')
    # print(lis)
    # q = ''.join(lis[1 if len(lis) > 1 else 0 :])
    # print(q)

