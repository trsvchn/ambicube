"""Cubes.
"""
from config import *


class Cube:
    def __init__(self, file: str):
        self.state = self.cube_config_parser(file)
        self.new_state = self.convert_state()

    def cube_config_parser(self, file: str) -> list:
        """Cube Config Parser.
        Returns nested list of colors.
        """
        with open(file, 'r') as f:
            lines = f.readlines()
            lines = [l.strip().split(',') for l in lines if l != '\n']
        return lines

    def convert_state(self) -> list:
        """Converts parsed list of lines into list of tuples with coordinates and color.
        """
        out = []
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                out.append((i, j, self.state[i][j]))
        return out

    def view_state(self):
        """Prints pretty view of the current state.
        """
        print('    0 1 2')
        print('  *-------*')
        for i, l in enumerate(self.state):
            print(f'{i} | {" ".join(l)} |')
            if i in [2, 5, 8]:
                print('  *-------*')

    def prepare_subcubes(self):
        """Creates subcube pieces.
        """
        self.subcubes = []
        for sb in self.new_state:
            subcube = SubCube(sb)
            self.subcubes.append(subcube)

    def export_to_latex(self, output: str):
        """Exports Cube state as a latex file.
        """
        self.prepare_subcubes()
        with open(output, 'w') as f:
            f.write(cube_header)
            for subcube in self.subcubes:
                f.write(subcube.latex())
            f.write(cube_footer)


class SubCube:
    def __init__(self, state):
        x, y, c = state

        if x in range(3):
            self.plane = 'yx'
            self.axis = 'z'
            if y == 0:
                self.x = -1.5
            elif y == 1:
                self.x = -0.5
            elif y == 2:
                self.x = 0.5
            else:
                raise ValueError('Incorrect value!')
        elif x in range(3, 6):
            self.plane = 'yz'
            self.axis = 'x'
            if y == 0:
                self.x = -1.5
            elif y == 1:
                self.x = -0.5
            elif y == 2:
                self.x = 0.5
            else:
                raise ValueError('Incorrect value!')
        elif x in range(6, 9):
            self.plane = 'xz'
            self.axis = 'y'
            if y == 0:
                self.x = 0.5
            elif y == 1:
                self.x = -0.5
            elif y == 2:
                self.x = -1.5
            else:
                raise ValueError('Incorrect value!')
        else:
            raise ValueError('Incorrect value!')

        if x in [0, 5, 8]:
            self.y = -1.5
        elif x in [1, 4, 7]:
            self.y = -0.5
        elif x in [2, 3, 6]:
            self.y = 0.5
        else:
            raise ValueError('Incorrect value!')
        self.colors = colors
        self.color = self.colors[c]
        self.latex_code = [
            subcube_template % (self.plane, self.axis, self.x, self.y, self.color),
            subcube_footer,
        ]

    def latex(self):
        """Returns LaTeX string.
        """
        return ' '.join(self.latex_code)
