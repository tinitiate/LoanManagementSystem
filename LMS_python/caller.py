import lms_master_data as lmd
import lms_engine as le
import random
import sys, logging

import time

# Convert Time to String in desired format


 
# STEP 1. Create a LOGGING Object
tiFileLog = logging.getLogger('tinitiate-file')

# STEP 2. Create a Log File Handler, the log messages will be created in 
#         this file
LogFile = logging.FileHandler('E:\\Training\\PythonAug2022/tinPython' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.log')

# STEP 3. Add the handler to the logging object
tiFileLog.addHandler(LogFile)

# STEP 4. Set Log Level
tiFileLog.setLevel(logging.DEBUG)

"""
cust_name=input("Please Enter Customer Name:")
cust_cs=input("Please Enter Customer Credit Score:")
cust_ReqLoanAmt=input("Please Enter Customer Loan Amount:")

le.lms_engine(p_cust_name=cust_name,p_cust_cs=int(cust_cs),p_cust_req_loan_amt=int(cust_ReqLoanAmt),p_loan_rules=lmd.loan_rules)
"""

tiFileLog.debug("LMS Starting")

lms_inputs = sys.argv
cust_name=lms_inputs[1]
cust_cs=lms_inputs[2]
cust_ReqLoanAmt=lms_inputs[3]
le.lms_engine(p_cust_name=cust_name,p_cust_cs=int(cust_cs),p_cust_req_loan_amt=int(cust_ReqLoanAmt),p_loan_rules=lmd.loan_rules,p_Log=tiFileLog)

tiFileLog.debug("LMS Ending")


"""
# Single Customer Input
# ######################
cust_name="aaa"
cust_cs=350
cust_ReqLoanAmt=12340

le.lms_engine(p_cust_name=cust_name,p_cust_cs=cust_cs,p_cust_req_loan_amt=cust_ReqLoanAmt,p_loan_rules=lmd.loan_rules)


# Multiple Customer Input
# ######################
customers = [ {"cust_name":"BBB","cust_cs":220,"cust_ReqLoanAmt":12340}
             ,{"cust_name":"ccc","cust_cs":320,"cust_ReqLoanAmt":22340}
             ,{"cust_name":"ddd","cust_cs":50,"cust_ReqLoanAmt":18340}
             ,{"cust_name":"eee","cust_cs":234,"cust_ReqLoanAmt":185555340}
             ]

for cust in customers:
    le.lms_engine( p_cust_name = cust["cust_name"]
                  ,p_cust_cs=cust["cust_cs"]
                  ,p_cust_req_loan_amt=cust["cust_ReqLoanAmt"]
                  ,p_loan_rules=lmd.loan_rules)

# 10000 Customer Inputs
# #####################
for c in range(10001):
    le.lms_engine(p_cust_name="a"+str(c),p_cust_cs=random.randint(0, 600),p_cust_req_loan_amt=random.randint(10000, 30000),p_loan_rules=lmd.loan_rules)

"""