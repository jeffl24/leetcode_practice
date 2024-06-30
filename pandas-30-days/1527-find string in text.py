
# 1527 find string in text
import re
import pandas as pd
data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Define the regex pattern to look for conditions that start with DIAB1
    pattern = r'\bDIAB1[0-9]*\b'
    df = patients[patients['conditions'].str.contains(pattern)]
    df = df[['patient_id', 'patient_name', 'conditions']]
    return df

# Alternative solution
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].apply(is_valid)]

def is_valid(content: str) -> bool:
    return any([x.startswith('DIAB1') for x in content.split()])


