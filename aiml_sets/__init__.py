import glob
import os
import shutil


__author__ = 'Aaron Hosford'


_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
_DEFAULT_INSTALL_PATH = os.path.abspath(os.path.expanduser('~/.aiml'))


def list_aiml_sets() -> list:
    return [set_name for set_name in os.listdir(_ROOT_PATH) if has_aiml_set(set_name)]


def has_aiml_set(set_name: str):
    return set_name[:1].isalpha() and os.path.isdir(os.path.join(_ROOT_PATH, set_name))


def get_aiml_set_path(set_name: str) -> str:
    if not has_aiml_set(set_name):
        raise KeyError(set_name)
    return os.path.join(_ROOT_PATH, set_name)


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


def install(set_name: str = None, pattern: str = None, destination_path: str = _DEFAULT_INSTALL_PATH) -> str:
    if set_name is None:
        set_names = list_aiml_sets()
    else:
        set_names = [set_name]
        if not has_aiml_set(set_name):
            raise KeyError(set_name)
    for set_name in set_names:
        for aiml_file in list_aiml_files(set_name, pattern):
            path_tail = aiml_file[len(_ROOT_PATH):].lstrip('/').lstrip('\\')
            copy_path = os.path.join(destination_path, path_tail)
            if not os.path.isdir(os.path.dirname(copy_path)):
                os.makedirs(os.path.dirname(copy_path))
            shutil.copy2(aiml_file, copy_path)
    return destination_path


def is_installed(set_name: str = None, pattern: str = None, destination_path: str = _DEFAULT_INSTALL_PATH) -> bool:
    if set_name is None:
        set_names = list_aiml_sets()
    else:
        set_names = [set_name]
        if not has_aiml_set(set_name):
            raise KeyError(set_name)
    for set_name in set_names:
        for aiml_file in list_aiml_files(set_name, pattern):
            path_tail = aiml_file[len(_ROOT_PATH):].lstrip('/').lstrip('\\')
            if not os.path.isfile(os.path.join(destination_path, path_tail)):
                return False
    return True
