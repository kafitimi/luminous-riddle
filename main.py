from glob import glob
from os import listdir, system

from yaml import Loader, load

riddle = './luminous-riddle'
with open(riddle + '/matching.yaml', mode='rt', encoding='utf-8') as file:
    matching = load(file, Loader=Loader)

retval = 0

for plan in glob('./{riddle}/plans/*.plx'):
    retval += system(f'python ./get_matrix.py {plan}')

for course, plans in matching.items():
    for plan in plans:
        parts = (
            'python',
            './get_rpd.py',
            f'{riddle}/plans/{plan}.plx',
            f'{riddle}/courses/{course}.yaml',
        )
        retval += system(' '.join(parts))

exit(retval)