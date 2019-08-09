"""Config.
"""

colors = {'b': 'blue',
          'g': 'gray',
          'o': 'orange',
          'y': 'yellow',
          'w': 'white',
          }
cube_header = '\\begin{tikzpicture}[line join=round]\n' \
              '\\clip (-2.5,-2.5) rectangle (2.5,2.5);\n' \
              '\\begin{scope}[tdplot_main_coords]\n' \
              '\\filldraw [canvas is yz plane at x=1.5, fill=white, draw=none] (-1.5,-1.5) rectangle (1.5,1.5);\n' \
              '\\filldraw [canvas is xz plane at y=1.5, fill=white, draw=none] (-1.5,-1.5) rectangle (1.5,1.5);\n' \
              '\\filldraw [canvas is yx plane at z=1.5, fill=white, draw=none] (-1.5,-1.5) rectangle (1.5,1.5);\n'
subcube_template = '\\draw [canvas is %s plane at %s=1.5,shift={(%s,%s)},fill=%s!90!black]'
subcube_footer = '(0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) ' \
                 'arc (0:90:\\radius) -- (\\radius,1) ' \
                 'arc (90:180:\\radius) -- (0,\\radius) ' \
                 'arc (180:270:\\radius) -- cycle;\n'
cube_footer = '\\end{scope}\n' \
              '\\end{tikzpicture}\n'
