"""Utils

Note:

Contents:

-get_conf

"""

__version__ = "0.1"

import os
import sys
import ConfigParser
import re

def get_conf(conf_path, info_group, info_key):
    """conf handler"""
    cf = ConfigParser.ConfigParser()
    cf.read(conf_path)
    info_value = cf.get(info_group,info_key)
    return info_value

def awk_exec(input_str):
    exec_str = input_str.replace("awk_ex","awk")
    exec_output = os.popen(exec_str).read().strip()
    return exec_output
