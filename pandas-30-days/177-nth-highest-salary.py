import pandas as pd
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})


def nth_highest_salary(df: pd.DataFrame, N: int) -> pd.DataFrame:
    df = df['salary'].drop_duplicates()
    df = df.sort_values(ascending=False)
    column = 'getNthHighestSalary('+str(N)+')'
    if N > len(df) or N<=0:
        return pd.DataFrame({column:[None]})
    return pd.DataFrame({column:[df.iloc[N-1]]})