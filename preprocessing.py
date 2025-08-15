import json
from colorama import Fore

instructions = []
with open("espdata.json", "r") as f:
    data = json.load(f)
    for key, chunk in data.items():
        for pairs in chunk['generated']:
            question, answer = pairs["question"], pairs["answer"]
            context_pair = {
                'question':f'Context:{chunk["context"]} {pairs['question']}',
                'answer': pairs['answer']
            }
            instructions.append(context_pair)
        print(Fore.YELLOW + str(chunk))
        print('\n~~~~~~~~~~~~~~~~~~~~~')

with open('data/instructions.json', 'w') as f:
    json.dump(instructions, f)

with open('data/instructions.json', 'r') as f:
    data = json.load(f)
    print(Fore.LIGHTMAGENTA_EX + str(data[:10]))