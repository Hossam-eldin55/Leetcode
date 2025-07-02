import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    e_lst = list(person['email'])
    test = []     
    dupl = []
    for e in e_lst:
        if e in test:
           if e in dupl:
            continue             #to avoid repeating
           dupl.append(e)  
        test.append(e) 
    return pd.DataFrame({'Email':dupl})
