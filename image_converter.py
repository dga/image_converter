#!/usr/bin/env python3

import os
import sys
from PIL import Image
from tqdm import tqdm

try:
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    fmt = sys.argv[3]

    if not os.path.exists(sys.argv[1]):
        raise Exception(f'Source directory \'{src_dir}\' not found.')

except IndexError as e:
    print(
        f'Usage: {sys.argv[0]} [source folder] [destination folder] [format]')
    sys.exit()

except Exception as e:
    print(e)
    sys.exit()


if src_dir[-1] != '/':
    src_dir += '/'
if dest_dir[-1] != '/':
    dest_dir += '/'

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

try:
    for filename in tqdm(os.listdir(src_dir)):
        filename_no_ext = os.path.splitext(filename)[0]
        img = Image.open(f'{src_dir}{filename}')
        img.save(f'{dest_dir}{filename_no_ext}.{fmt}', fmt)

except KeyError as e:
    print(f'Format type \'fmt\' unsupported.')
