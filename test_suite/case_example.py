import sys,os
sys.path.append("./")
from baseCase import BaseTestCaseClass

if __name__ == "__main__":
    awkExTest = BaseTestCaseClass("./common_conf.conf")
    awkExTest.set_utp_name("awk_ex")
    awkExTest.run_me()
