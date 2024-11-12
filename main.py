from glob import glob
from os import system

from yaml import Loader, load

riddle = './luminous-riddle'
with open(riddle + '/matching.yaml', mode='rt', encoding='utf-8') as file:
    matching = load(file, Loader=Loader)

retval = 0

for plan in glob(f'./{riddle}/plans/*.plx'):
    retval += system(f'python ./get_matrix.py {plan}')
    for course, plans in matching.items():
        if plan not in plans:
            continue
        retval += system(
            f'python ./get_rpd.py {plan} '
            f'{riddle}/courses/{course}.yaml'
        )
    system(f'ls -lah')

exit(retval)