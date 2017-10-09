
from os import listdir
from io import BytesIO

import os.path
import sys


if sys.version_info.major >= 3:
    from configparser import ConfigParser
elif sys.version_info.major == 2:
    from ConfigParser import ConfigParser


def compare_config_files(config_file, best_practice_dir):
    best_practice_files = []
    if os.path.isdir(best_practice_dir):
        best_practice_files = [
            os.path.abspath(os.path.join(best_practice_dir, f))
            for f
            in listdir(best_practice_dir)
        ]
    elif os.path.isfile(best_practice_dir):
        best_practice_files.append(best_practice_dir)
    best_practice_config = ConfigParser(allow_no_value=True)
    best_practice_config.read(best_practice_files)

    current_config = ConfigParser(allow_no_value=True)
    current_config.read(config_file)
    if best_practice_config._sections == current_config._sections:
        return True
    #return False


    print('Update Config')

    # print('### Best Practice Config:')
    # best_practice_config.write(sys.stdout)
    #
    # print('\n\n### Current Config:')
    # current_config.write(sys.stdout)
    with open(config_file + '.new', 'w') as new_file:
        best_practice_config.write(new_file)
    with open(config_file + '.old', 'w') as old_file:
        current_config.write(old_file)
    import pdb; pdb.set_trace()
    best_practice_config.write(sys.stdout)
    return False


if __name__ == '__main__':
    print(compare_config_files('../tox.ini', '../code_snippets/tox.d/'))
    print(compare_config_files('../tox.ini.old', '../tox.ini'))
