import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///project_database', echo=False)

with engine.connect() as connection:
    df = pd.read_sql('SELECT * FROM database', connection) 

region = df['регион'].value_counts()
print("A:")
print(region)


start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-12-31')
df['Дата_регистрации'] = pd.to_datetime(df['Дата_регистрации'])
registrations = df[(df['Дата_регистрации'] >= start_date) & (df['Дата_регистрации'] <= end_date)]
print("Б:")
print(registrations.shape[0])


date = pd.to_datetime('now')
df['Дата_рождения'] = pd.to_datetime(df['Дата_рождения'])
age_filter = ((date - df['Дата_рождения']) // pd.Timedelta(days=365.25)).between(18, 35)
users_years = df[age_filter]
print("В:")
print(users_years)
