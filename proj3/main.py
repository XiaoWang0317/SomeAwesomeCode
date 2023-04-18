from multiprocessing import Pool
import os

# creating processes (y will send a modify requirement)
all_processes = ['u 1', 'v 1', 'w 1', 'x 1', 'y 2', 'z 1']


# This block of code enables us to call the script from command line.
def execute(process):
    os.system(f'python router.py {process}')


if __name__ == '__main__':
    with Pool(6) as p:
        p.map(execute, all_processes)