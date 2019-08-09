import argparse
from cube import Cube


parser = argparse.ArgumentParser("Cube states to pdf converter.")
parser.add_argument('-i', '--input_state', type=str, metavar='PATH', help='Path to input csv state file.')
parser.add_argument('-o', '--output_file', type=str, metavar='PATH', help='Path for out tex file.')


def main():
    args = parser.parse_args()
    state = args.input_state
    out_tex = args.output_file
    cb = Cube(state)
    print(f'Converting {state} to {out_tex}...')
    cb.view_state()
    cb.export_to_latex(out_tex)


if __name__ == '__main__':
    main()
