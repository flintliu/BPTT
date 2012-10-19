import sys,os
sys.path.append("./")
from baseCase import BaseTestCaseClass

class awkExClass(BaseTestCaseClass):
    def __init__(self):
        self.conf_path = "./common_conf.conf"
        self.utp_name = ""
        BaseTestCaseClass.__init__(self,self.conf_path,self.utp_name)

    def data_runner(self,dc,UT_path):
        dc_info = dc.split("    ")
        dc_name = dc_info[0].strip()
        dc_input_UT = dc_info[1].strip()
        dc_input_expect = dc_info[2].strip()
        if dc_input_expect == "awk":
            dc_input_expect = dc_input_UT.replace("awk_ex","awk")
        dc_input_UT = dc_input_UT.replace("awk_ex",UT_path)
        dc_output_UT = os.popen(dc_input_UT).read()
        dc_output_expect = os.popen(dc_input_expect).read()
        if dc_output_UT == dc_output_expect:
            data_result = 1
        else:
            data_result = 0
        return data_result,dc_name

if __name__ == "__main__":
    awkExTest = awkExClass()
    awkExTest.set_utp_name("awk_ex")
    awkExTest.run_me()
