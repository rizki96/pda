import os
import sys
import importlib
import logging

from uuid import getnode as get_mac


def root_dir():
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(os.path.realpath(__file__))
    return datadir


def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


def db_str_conn(db_name, path=None):
    mac = str(get_mac())
    mac = mac.zfill(16) if len(mac) < 16 else mac[0:15]
    key = '%s%s%s%s%s%s' % (mac[1], mac[2], mac[0], mac[4], mac[7], mac[8])

    current_path = path
    if not path:
        current_path = root_dir()
    if sys.platform == "win32":
        return 'sqlite+pysqlcipher://:{0}@/{1}/{2}'.format(key, current_path, db_name)
    else:
        return 'sqlite+pysqlcipher://:{0}@//{1}/{2}'.format(key, current_path, db_name)


