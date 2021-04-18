import pandas as pd
import numpy as np


PATH_EM = '/home/gordon_local/local_workplace/swsWorkBringHome/name_ID_sort/employeeID_data.csv'
PATH_TAN = '/home/gordon_local/local_workplace/swsWorkBringHome/name_ID_sort/tanda_data.csv'
df_em = pd.read_csv(PATH_EM)
df_tan = pd.read_csv(PATH_TAN)


df_merge_tan_em = pd.merge(df_tan, df_em, on=['firstname', 'lastname'],  how='left')

df_merge_tan_em.to_csv('./merge_tan_em_data.csv', index=False)