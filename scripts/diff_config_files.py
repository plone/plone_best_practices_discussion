
from configparser import ConfigParser


def _read_config_file(input):
    config = ConfigParser(input)
    return config


def compare_config_files(config_file, best_practice_dir):
    best_practice_config = ConfigParser()
    for best_practice_file in best_practice_dir:
        config = ConfigParser(best_practice_file)

        best_practice_config.append(config)

    config = ConfigParser(config_file)
    for section in best_practice_config.get_sections():
        config.get(section.name)

    return True
