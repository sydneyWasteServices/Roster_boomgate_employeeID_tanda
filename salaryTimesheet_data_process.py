import pandas as pd
import numpy as np 


# salary timesheet Naming problem
#  NaN	 Bejamin edwards	bejamin => correct salary timesheet  => to Bejamin
#  NaN	Fei , Xia  xia => Xiaohua => correct salary timesheet  => to Xiaohua
# NaN	Dean, Zac  Zac => zaheer => correct salary timesheet  => to zaheer
# NaN	Ruhr, John => johann => correct salary timesheet  => to johann


# EmployeeID list issue
# NaN	Roberts , Garry => correct Employee ID => to Garry


df = pd.read_excel(PATH_SAL)
df.pop('Unnamed: 26')

df = df.rename(columns={'Employee ID' : 'EmployeeID'})

df['Employee Name'] = df['Employee Name'].str.replace('*','')

df['EmployeeID'] = df['EmployeeID'].str.lower()

df[['lastname', 'firstname']] = df['Employee Name'].str.lower().str.split(",", 1, expand=True)

df['lastname'] = df['lastname'].str.strip()
df['firstname'] = df['firstname'].str.strip()

df['lastname'] = [lastname.split(" ")[1] if len(lastname.strip().split(" ")) > 1 else lastname for lastname in df.lastname]

df['middlename'] = [middlename.split(" ")[1] if len(middlename.split(" ")) > 1 else 'nomiddlename' for middlename in df.firstname]

df['firstname'] = [firstname.split(" ")[0] if len(firstname.split(" ")) > 1 else firstname for firstname in df.firstname]

df['lastname'] = df['lastname'].str.strip()
df['firstname'] = df['firstname'].str.strip()

# 1. TO_csv transformed Salary timesheet => 
# 2. and then merge it with employee ID
# 3. remove Salary Timesheet employee ID 

