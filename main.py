from os import system

from yaml import Loader, load

riddle = './luminous-riddle'
with open(riddle + '/matching.yaml', mode='rt', encoding='utf-8') as file:
    matching = load(file, Loader=Loader)

retval = 0
for course, plans in matching.items():
    for plan in plans:
        parts = (
            'python',
            './get_rpd.py',
            f'{riddle}/plans/{plan}',
            f'{riddle}/courses/{course}.yaml',
        )
        retval += system(' '.join(parts))

exit(retval)