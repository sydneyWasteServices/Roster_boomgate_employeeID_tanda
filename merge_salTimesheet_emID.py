import pandas as pd
import numpy as np

# df => Transformed Salary Timesheet
#  df_em => Transformed employee ID

df_merge_em_sal = pd.merge(df, df_em, on=['lastname', 'firstname'], how='left', suffixes=("_sal", "_em"))