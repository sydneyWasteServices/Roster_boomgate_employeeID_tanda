import pandas as pd
import numpy as np


PATH = '/home/gordon_local/local_workplace/blobStore/driver_timesheets/EmployeeID.xlsx'

df = pd.read_excel(PATH, header=0, engine='openpyxl')


df[['lastname', 'firstname']] = df.Name.str.lower().str.split(",", 1, expand=True)

df['lastname'] = [lastname.split(" ")[1] if len(lastname.strip().split(" ")) > 1 else lastname for lastname in df.lastname]


df['lastname'] = df['lastname'].str.strip()

df['firstname'] = df['firstname'].str.strip()



df['middlename'] = [middlename.split(" ")[1] if len(middlename.split(" ")) > 1 else 'nomiddlename' for middlename in df.firstname]

df['firstname'] = [firstname.split(" ")[0] if len(firstname.split(" ")) > 1 else firstname for firstname in df.firstname]

df['Card ID'] = df['Card ID'].str.lower()

df = df.rename(columns={'Card ID' : 'EmployeeID'})


df['lastname'] = df['lastname'].str.strip()

df['firstname'] = df['firstname'].str.strip()

df.to_csv('./employeeID_data.csv', index=False)
