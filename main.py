from glob import glob
from os import system

from yaml import Loader, load

riddle = './luminous-riddle'
with open(riddle + '/matching.yaml', mode='rt', encoding='utf-8') as file:
    matching = load(file, Loader=Loader)

retval = 0

for plan in glob(f'./{riddle}/plans/*.plx'):
    plan_name = plan.split('/')[-1][:-4]

    retval_matrix = system(f'python ./get_matrix.py {plan}')
    if not retval_matrix:
        system(f'mv {plan.replace('.plx', '.txt')} ./{plan_name}.csv')
    retval += retval_matrix

    for course, plans in matching.items():
        if plan_name not in plans:
            continue
        retval += system(
            f'python ./get_rpd.py {plan} '
            f'{riddle}/courses/{course}.yaml '
            f'-o ./{plan_name[:-4]}_{course}.docx'
        )
    system('zip {plan_name}.zip {plan_name}.csv *.docx')
    system('rm {plan_name}.csv *.docx')

system(f'ls -lah {riddle}/courses')

exit(retval)