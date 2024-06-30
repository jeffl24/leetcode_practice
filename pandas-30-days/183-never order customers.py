
import pandas as pd

# Approach 1
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left')
    zero_order_customers = merged[merged['customerId'].isna()]
    result = zero_order_customers[['name']].rename(columns = {'name': 'Customers'})
    return result

# Approach 2
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    no_order_cust = customers[~customers['id'].isin(orders['customerId'])]
    no_order_cust_name = no_order_cust[['name']].rename(columns = {'name': 'Customers'})
    return no_order_cust_name
