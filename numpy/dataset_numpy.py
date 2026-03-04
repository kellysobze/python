from numpy.esercizio import RAW_RECORDS

{"age": " 25", "income": "€30.000", "debts": "2",   "credit_score": "650", "approved": "yes"},
{"age": "45",  "income": "80000",   "debts": "1",   "credit_score": "720", "approved": "1"},    
{"age": "N/A", "income": "€50.000", "debts": "5",   "credit_score": "580", "approved": "no"},  
{"age": "23",  "income": " 25k ",   "debts": "3",   "credit_score": "600", "approved": "0"},    
{"age": "52",  "income": "120000",  "debts": "0",   "credit_score": "800", "approved": "yes"},  
{"age": "40",  "income": "70k",     "debts": "4",   "credit_score": "610", "approved": "no"},   
{"age": "??",  "income": "40000",   "debts": "",    "credit_score": None,  "approved": "yes"},  
{"age": "31",  "income": "€-1000",  "debts": "2",   "credit_score": "690", "approved": "no"},   
{"age": "34 ", "income": "45000",   "debts": "two", "credit_score": "710", "approved": "yes"}, 
{"age": "29",  "income": " 60000 ", "debts": "1",   "credit_score": "680", "approved": "YES"}


def main()-> None:
    x,y = pipeline_clean_records(RAW_RECORDS)
    x_enchanced= pipeline add_feature_egigneering(x)
    x_ready=pipeline.minmax_normalize(x_enchanced)
    x_train,x_test,y_train,y_test=pipeline.train_test_split(x_ready,y)
    print(x_train)
    print(y_train)
    print(x_test)
    print(y_test)