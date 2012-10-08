#! /usr/bin/python
import os,re,ConfigParser

def case_list_collector(caseDir):
    try:
        dirList = os.listdir(caseDir)
        caseList = []
        for item in dirList:
            if not os.path.isdir(item):
                if re.match('case_',item):
                    caseList.append(item)
        return caseList
    except Exception,e:
        print "Get case list failed!"
        print e
        return None

def case_runner(caseList):
    try:
        executeResults = {}
        for case in caseList:
            print str(case) + " is runing..."
            singleResult = os.popen('python ./test_suite/' + str(case)).readlines()
            singleResult = singleResult[1].strip()
            executeResults.update({str(case):singleResult})
        return executeResults
    except Exception,e:
        print "Runner error!"
        print e
        return None

def log_printer(executeResults):
    try:
        passNum = 0
        failNum = 0
        failCase = {}
        for resultCaseName in executeResults:
            singleResult = executeResults.get(resultCaseName)
            singleResult = eval(singleResult)
            singlePassNum = singleResult.get("pass")
            singleFailNum = singleResult.get("fail")
            singleLog = singleResult.get("log")
            passNum += int(singlePassNum)
            failNum += int(singleFailNum)
            if singleLog != "":
                failCase.update({resultCaseName:singleLog})
        print "pass number is " + str(passNum)
        print "fail number is " + str(failNum)
        print "------------------------------"
        for resultCaseName in failCase:
            print resultCaseName
            failData = failCase.get(resultCaseName)
            for case in failData.split(";"):
                print "    " + case
            print "------------------------------"
    except Exception,e:
        print "print log err!"
        print e

if __name__ == "__main__" :
    cf = ConfigParser.ConfigParser()
    cf.read("common_conf.conf")
    caseDir = cf.get("main","casePath")
    caseList = case_list_collector(caseDir)
    if caseList != None and caseList != []:
        executeResults = case_runner(caseList)
        print executeResults
        if executeResults != None and executeResults != {}:
            log_printer(executeResults)
    print "Done!"
