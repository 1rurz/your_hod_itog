from main import df_itog
import pandas as pd
from datetime import datetime, timedelta


region = df_itog['регион'].value_counts()


print("A:")
print(region)


start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
registrations = df_itog[(df_itog['Дата регистрации'] >= start_date.strftime('%Y-%m-%d')) & (df_itog['Дата регистрации'] <= end_date.strftime('%Y-%m-%d'))]


print("Б:")
print(registrations.shape[0])



date = datetime.now()
df_itog['Дата рождения'] = pd.to_datetime(df_itog['Дата рождения'])
age_filter = ((date - df_itog['Дата рождения']) // timedelta(days=365.25)).between(18, 35)
users_yers = df_itog[age_filter]


print("В:")
print(users_yers)