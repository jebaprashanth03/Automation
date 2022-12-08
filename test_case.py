import pandas as pd

login_test = pd.read_excel("test_case_excel\\login_test_cases.xlsx")

for index, row in login_test.iterrows():
    if bool(row['expected_login']) == test_login_excel(row['email'], row['password']):
        login_test.loc[index, "pass_or_fail"] = 'Pass'
    else:
        login_test.loc[index, "pass_or_fail"] = 'Fail'


print(login_test)