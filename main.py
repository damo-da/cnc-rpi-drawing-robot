from __future__ import print_function, division

import svgpathtools
import numpy as np
from matplotlib import pyplot as plt


def get_paths(file_path, debug=False):
    _paths, attributes = svgpathtools.svg2paths(file_path)
    if debug:
        print(attributes)

    res_paths = []

    for path in _paths:
        for p in path:
            if isinstance(p, svgpathtools.CubicBezier):
                P0, P1, P2, P3 = p.start, p.control1, p.control2, p.end
                points = []
                for t in np.arange(0, 1, 0.01):
                    B = ((1 - t)**3) * P0 + 3 * ((1-t)**2) * t * P1 + 3 * (1-t) * (t**2) * P2 + (t**3) * P3
                    points.append(B)
                res_paths.append(points)
            elif isinstance(p, svgpathtools.Line):
                # print(p.start, p.end)
                res_paths.append((p.start, p.end))
            else:
                print('something else found: ', type(p))
                raise Exception("Oh, oh.")

    return res_paths


def show_paths(res_paths):
    print(res_paths)
    for path in res_paths:
        xs = list(map(lambda c: c.real, path))
        ys = list(map(lambda c: c.imag, path))
        # print(xs)
        plt.plot(xs, ys, color='black')
    plt.show()


if __name__ == '__main__':
    paths = get_paths('./image1.svg')
    show_paths(paths)
