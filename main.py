from yaml import Loader, load

with open('matching.yaml', mode='rt', encoding='utf-8') as file:
    matching = load(file, Loader=Loader)

for course, plans in matching.items():
    for plan in plans:
        parts = (
            'python',
            './glowing-enigma/get_rpd.py',
            f'--plan ./plans/{plan}',
            f'--course ./courses/{course}.yaml',
        )
        print(' '.join(parts))
