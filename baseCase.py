"""Test case basic class.

Note:

Contents:

- BaseTestCaseClass: test case base class

XXX To do:

"""

__version__ = "0.1"
__all__ = ["BaseTestCaseClass"]

import os
import sys
import re
import util
import logging

class BaseTestCaseClass():
    """Test case basic class.
    
    """
    def __init__(self,conf_path,utp_name):
        self.conf_path = conf_path
        self.utp_name = utp_name
        self.debug_info = []

    def set_utp_name(self,utp_name_set):
        self.utp_name = utp_name_set
        return None

    def get_UTP_path(self):
        """To get the common conf like path of UTP."""
        UT_group = "utp"
        UT_path = util.get_conf(self.conf_path,UT_group,self.utp_name)
        return UT_path

    def get_data_info(self):
        """To get the infomation of data set. """
        c = sys._getframe(2)
        case_name = c.f_code.co_filename
        data_path = case_name.replace("case_","data_")[:-3] #This has to be fix to changing the first.
        print data_path
        if os.path.isdir(data_path):
            data_info = ["dir",data_path]
        elif os.path.isfile(data_path):
            data_info = ["file",data_path]
        else:
            data_info = None
        return data_info

    def data_runner(self,dc,UT_path):
        """To run a single data using a test case."""
        dc_info = dc.split("    ")
        dc_name = dc_info[0].strip()
        dc_input_UT = dc_info[1].strip()
        dc_input_expect = dc_info[2].strip()
        dc_output_UT = os.popen(dc_input_UT).read()
        dc_output_expect = os.popen(dc_input_expect).read()
        if dc_output_UT == dc_output_expect:
            dc_result = 1
        else:
            dc_result = 0
        return dc_result, dc_name

    def data_manager(self,data_info,UT_path):
        """To run a single case."""
        pass_num = 0
        fail_num = 0
        data_name = []
        if data_info[0] == "file":
            data_file = open(data_info[1])
            data_cases = data_file.readlines()
            for dc in data_cases:
                if re.match("data_",dc):
                    data_result, dc_name = self.data_runner(dc,UT_path)
                    if data_result == 1:
                        pass_num += 1
                    elif data_result == 0:
                        fail_num += 1
                        data_name.append(dc_name)
                else:
                    pass
        elif data_info[0] == "dir":
            pass
        data_name = ";".join(data_name)
        return pass_num,fail_num,data_name

    def log_printer(self,pass_num,fail_num,data_name):
        """logger"""
        self.debug_info = ";".join(self.debug_info)
        log = {}
        log.update({"pass":pass_num})
        log.update({"fail":fail_num})
        log.update({"data_name":data_name})
        log.update({"debug_info":self.debug_info})
        return log

    def run_me(self):
        """main function"""
        data_info = self.get_data_info()
        UT_path = self.get_UTP_path()
        pass_num,fail_num,data_name = self.data_manager(data_info,UT_path)
        print self.log_printer(pass_num,fail_num,data_name)
        return None

if __name__ == "__main__":
    test = BaseTestCaseClass()
    test.set_utp_name("awk_ex")
    print test.get_UTP_path()
