import pandas as pd
# 1873 Calculate special bonus
data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})


# Approach 1
def calculate_bonus(df):
    if df['employee_id'] % 2 != 0 and not df['name'].startswith('M'):
        return df['salary']
    else: 
        return 0

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(calculate_bonus, axis = 1)
    result = employees[['employee_id', 'bonus']].sort_values(by = 'employee_id')
    return result

# Approach 2
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    conditions = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))

    # conditions = (employees['employee_id'] % 2 != 0) & (employees['name'].apply(lambda x: not x.startswith('M'))) # alternative

    # Apply the conditions to calculate the bonus
    employees['bonus'] = employees['salary'].where(conditions, 0)

    # Sort the result by employee_id
    result_df = employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    return result_df

# Alternative 3
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.assign(bonus = employees.apply(
            lambda x: x['salary'] if int(x['employee_id']) % 2 != 0 
        and 
            not x['name'].startswith('M')
        else 0, 
        axis = 1
    ))[['employee_id', 'bonus']].sort_values(by = 'employee_id')
    return result

# df.assign supports method chaining, for example df = df.assign(grade=df['score'].apply(get_grade)).sort_values(by='grade')
# df.assign also returns a new DataFrame with the changes, leaving the original DataFrame unchanged.
