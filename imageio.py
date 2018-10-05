import os.path as osp

from napari.io import reads_file_ext, writes_file_ext

import imageio


def get_file_exts():
    exts = []
    for format in imageio.formats:
        exts.extend(format.extensions)

    return exts


@reads_file_ext
def read(path):
    ext = osp.splitext(path)[-1]

    if ext not in get_file_exts():
        raise TypeError('Cannot read that extension.')

    return imageio.imread(path)


@writes_file_ext
def write(data, path):
    ext = osp.splitext(path)[-1]

    if ext not in get_file_exts():
        raise TypeError('Cannot write that extension.')

    return imageio.imwrite(path, data)
