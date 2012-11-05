#! /usr/bin/python
"""
----------
***BPTT***
BPTT: Backend Program Testing Tool
Description: On the Linux based env, test cases are formed by text input, text output and commond. The BPTT can help QA to collect, 
             generate and manage test cases easily. The tool is data drive, QA just need to develop one test case and put data set
             into a file. The basic function for test case is in the baseCaseClass, so if you want to add a new case, just need to
             inherit this class and rewrite function if you have special requirement. Some common tools are provided in the util.py.
             There is a example called case_example and the data set is data_example, the requirement comes from a real project in
             our company, the UTP aim to enhance the power of AWK and the test case will verify its basic function and compare with
             AWK.
Author: Yang LIU(flint)
E-mail: flintliu@hotmail.com
**********
----------
"""

import os
import re
import ConfigParser

def case_list_collector(case_dir):
    """Try to get case names."""
    try:
        dir_list = os.listdir(case_dir)
        case_list = []
        for item in dir_list:
            if not os.path.isdir(item):
                if re.match('case_',item):
                    case_list.append(item)
        return case_list
    except Exception,e:
        print "Get case list failed!"
        print e
        return None

def case_runner(case_list):
    """To run cases one by one."""
    try:
        execute_results = {}
        for case in case_list:
            print str(case) + " is runing..."
            single_result = os.popen('python ./test_suite/' + str(case)).readlines()
            single_result = single_result[0].strip()
            execute_results.update({str(case):single_result})
        return execute_results
    except Exception,e:
        print "Runner error!"
        print e
        return None

def log_printer(execute_results):
    """Print logs, I will rewite this function to support multithreading"""
    try:
        pass_num = 0
        fail_num = 0
        fail_case = {}
        for result_case_name in execute_results:
            single_result = execute_results.get(result_case_name)
            single_result = eval(single_result)
            single_pass_num = single_result.get("pass")
            single_fail_num = single_result.get("fail")
            single_data_name = single_result.get("data_name")
            single_debug_info = single_result.get("debug_info")
            pass_num += int(single_pass_num)
            fail_num += int(single_fail_num)
            if single_data_name != "":
                fail_case.update({result_case_name:single_data_name})
        print "pass number is " + str(pass_num)
        print "fail number is " + str(fail_num)
        print "------------------------------"
        for result_case_name in fail_case:
            print result_case_name
            fail_data = fail_case.get(result_case_name)
            for case in fail_data.split(";"):
                print "    " + case
            if single_debug_info != "":
                for di in single_debug_info.split(";"):
                    print "DEBUG: " + di
            print "------------------------------"
    except Exception,e:
        print "print log err!"
        print e

def run():
    """Main function."""
    cf = ConfigParser.ConfigParser()
    cf.read("common_conf.conf")
    case_dir = cf.get("main","casePath")
    case_list = case_list_collector(case_dir)
    if case_list != None and case_list != []:
        execute_results = case_runner(case_list)
        if execute_results != None and execute_results != {}:
            log_printer(execute_results)
    print "Done!"

if __name__ == "__main__" :
    run()
