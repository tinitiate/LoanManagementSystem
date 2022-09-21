
def lms_engine(p_cust_name,p_cust_cs,p_cust_req_loan_amt,p_loan_rules,p_Log):
    
    l_is_success = 0
    
    for c in p_loan_rules:
        if p_cust_cs >= c["cs_start"] and p_cust_cs <= c["cs_end"] and p_cust_req_loan_amt >= c["loan_amt_start"] and p_cust_req_loan_amt <= c["loan_amt_end"]:
            print(p_cust_name)
            print(c["interest"])
            print(c["duration_in_months"])
            l_is_success = 1
            p_Log.debug("Loan Accepted for "+p_cust_name)
            break

    if l_is_success == 0:
        print("Sorry",p_cust_name,"your CS is too low")
        p_Log.critical("Loan Rejected for "+p_cust_name)

"""
[{"cs_start":100,"cs_end":200,"loan_amt_start":10000,"loan_amt_end":15000,"interest":5,"duration_in_months":72}
,{"cs_start":201,"cs_end":300,"loan_amt_start":10000,"loan_amt_end":15000,"interest":4.5,"duration_in_months":72}
,{"cs_start":301,"cs_end":400,"loan_amt_start":10000,"loan_amt_end":15000,"interest":4.0,"duration_in_months":72}
,{"cs_start":401,"cs_end":500,"loan_amt_start":10000,"loan_amt_end":15000,"interest":3.5,"duration_in_months":72}
,{"cs_start":100,"cs_end":200,"loan_amt_start":15001,"loan_amt_end":20000,"interest":6,"duration_in_months":72}
,{"cs_start":201,"cs_end":300,"loan_amt_start":15001,"loan_amt_end":20000,"interest":5.5,"duration_in_months":72}
,{"cs_start":301,"cs_end":400,"loan_amt_start":15001,"loan_amt_end":20000,"interest":4.0,"duration_in_months":72}
,{"cs_start":401,"cs_end":500,"loan_amt_start":20001,"loan_amt_end":20000,"interest":3.5,"duration_in_months":72}
,{"cs_start":100,"cs_end":200,"loan_amt_start":20001,"loan_amt_end":25000,"interest":6,"duration_in_months":72}
,{"cs_start":201,"cs_end":300,"loan_amt_start":20001,"loan_amt_end":25000,"interest":5.5,"duration_in_months":72}
,{"cs_start":301,"cs_end":400,"loan_amt_start":20001,"loan_amt_end":25000,"interest":4.0,"duration_in_months":72}
,{"cs_start":401,"cs_end":500,"loan_amt_start":20001,"loan_amt_end":25000,"interest":3.5,"duration_in_months":72}
]        
"""