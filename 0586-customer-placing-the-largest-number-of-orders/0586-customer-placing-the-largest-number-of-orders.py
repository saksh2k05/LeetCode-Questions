import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counting = orders.groupby('customer_number').size()
    counts = []
    counts.append(counting.idxmax())
    return pd.DataFrame({'customer_number': counts})