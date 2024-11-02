from os import system

from yaml import Loader, load

riddle = './luminous-riddle'
with open(riddle + '/matching.yaml', mode='rt', encoding='utf-8') as file:
    matching = load(file, Loader=Loader)

for course, plans in matching.items():
    for plan in plans:
        parts = (
            'python',
            './get_rpd.py',
            f'--plan {riddle}/plans/{plan}',
            f'--course {riddle}/courses/{course}.yaml',
        )
        system(' '.join(parts))
