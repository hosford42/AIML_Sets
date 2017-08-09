import glob
import os
import shutil


_ROOT_PATH = os.path.dirname(__file__)


def list_aiml_sets() -> list:
    return [set_name for set_name in os.listdir(_ROOT_PATH) if has_aiml_set(set_name)]


def has_aiml_set(set_name: str):
    return set_name[:1].isalpha() and os.path.isdir(os.path.join(_ROOT_PATH, set_name))


def get_aiml_set_path(set_name: str) -> str:
    set_path = os.path.join(_ROOT_PATH, set_name)
    if not os.path.isdir(set_path) or set_name[:1].isalpha():
        raise KeyError(set_name)
    return set_path


def list_aiml_files(set_name: str = None, pattern: str = None) -> list:
    if pattern is None:
        pattern = '*.aiml'
    elif not pattern.endswith('.aiml'):
        pattern += '.aiml'
    if set_name is None:
        return glob.glob(os.path.join(_ROOT_PATH, '*', pattern))
    else:
        set_path = get_aiml_set_path(set_name)
        return glob.glob(os.path.join(set_path, pattern))


def install(destination_path=os.path.expanduser('~/.aiml'), set_name: str = None, pattern: str = None) -> str:
    if set_name is None:
        set_names = list_aiml_sets()
    else:
        set_names = [set_name]
        if not has_aiml_set(set_name):
            raise KeyError(set_name)
    for set_name in set_names:
        install_path = os.path.join(destination_path, set_name)
        if not os.path.isdir(install_path):
            os.makedirs(install_path)
        for aiml_file in list_aiml_files(set_name, pattern):
            shutil.copy2(aiml_file, os.path.join(install_path, aiml_file))
    return destination_path
