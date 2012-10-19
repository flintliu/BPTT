BPTT
====

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