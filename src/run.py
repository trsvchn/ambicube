import os
from glob import glob
from subprocess import run
import argparse

from cube import Cube
from config import temp_dir, render_cmd, main_render_cmd


parser = argparse.ArgumentParser("Cube states to pdf converter")
parser.add_argument('-i', '--input_dir', default='./states', type=str, metavar='PATH', help='Path to input csv file.')
parser.add_argument('-o', '--output_dir', default='./images', type=str, metavar='PATH', help='Path for temp pdf files.')


def main():
    args = parser.parse_args()
    states = glob(os.path.join(args.input_dir, '*.csv'))
    for state in states:
        jobname = os.path.basename(state).split('.')[0]
        angle = 150 if 'l' in jobname else 120
        cb = Cube(state)
        print(f'Converting {state}...')
        cb.view_state()
        out_tex = os.path.join(temp_dir, jobname + '.tex')
        cb.export_to_latex(out_tex)
        cmd = render_cmd % (jobname, args.output_dir, out_tex, angle)
        print(f'Rendering pdf for {state}...')
        run(cmd, shell=True)

    def remove_files(folder):
        patterns_tp_remove = ['*.aux', '*.log', '*.gz']
        to_remove = []
        for p in patterns_tp_remove:
            to_remove.extend(glob(os.path.join(folder, p)))
        [os.remove(file) for file in to_remove]

    remove_files(args.output_dir)

    print('Rendering main.pdf...')

    run(main_render_cmd, shell=True)
    remove_files('.')


if __name__ == '__main__':
    main()
