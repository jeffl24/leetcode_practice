import pandas as pd
data = [[1, 100]]
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    second_highest = pd.DataFrame(
        {'SecondHighestSalary': 
         [None if unique_salaries.size < 2 else unique_salaries.nlargest(2).iloc[1]]
        })
    return second_highest