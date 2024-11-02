from yaml import Loader, load

matching = load('matching.yaml', Loader=Loader)

for course, plans in matching.items():
    for plan in plans:
        parts = (
            'python',
            './glowing-enigma/get_rpd.py',
            f'--plan ./plans/{plan}',
            f'--course ./courses/{course}.yaml',
        )
        print(' '.join(parts))
