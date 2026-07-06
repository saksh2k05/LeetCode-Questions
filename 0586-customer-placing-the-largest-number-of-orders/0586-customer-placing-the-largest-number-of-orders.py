import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counting = orders.groupby('customer_number').size().reset_index(name='count')
    return counting.nlargest(1, 'count')[['customer_number']]
    