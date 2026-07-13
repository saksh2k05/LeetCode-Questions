import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers.groupby('num').size()
    count1 = counts[counts==1]
    if count1.empty:
        return pd.DataFrame({'num':[None]})
    return pd.DataFrame({"num": [count1.index.max()]})