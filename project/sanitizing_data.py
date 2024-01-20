import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
original_data = pd.read_excel("monitors.xlsx")


sanitized_data = original_data.dropna()
def convert_to_lower(value):
    return value.lower()
sanitized_data['ბრენდი'] = sanitized_data['ბრენდი'].apply(convert_to_lower)


sanitized_data.to_excel("monitors_sanitized.xlsx", index=False)