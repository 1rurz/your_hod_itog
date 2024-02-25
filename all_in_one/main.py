import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
from sqlalchemy import create_engine

fake = Faker('ru_RU')

num_records = 1000000

data = {
    'id': np.arange(1, num_records + 1),
    'ФИО': [fake.name() for _ in range(num_records)],
    'Дата_рождения': [fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d') for _ in range(num_records)],
    'номер_телефона': [fake.phone_number() for _ in range(num_records)],
    'регион': [fake.region() for _ in range(num_records)],
    'Дата_регистрации': [fake.date_this_decade().strftime('%Y-%m-%d') for _ in range(num_records)],
    'курс_обучения': [fake.random_int(1, 5) for _ in range(num_records)],
    'вуз': [fake.company() for _ in range(num_records)]
}


df = pd.DataFrame(data)


df.to_csv('ata.csv', index=True)


engine = create_engine('sqlite:///project_db', echo=False)
df.to_sql('project_db', con=engine, index=False, if_exists='replace')


with engine.connect() as connection:
    region = pd.read_sql_query("SELECT регион, COUNT(*) AS count FROM project_db GROUP BY регион", connection)
    print("A. Количество регистраций по регионам:")
    print(region)


    start_date = pd.to_datetime('2023-01-01').strftime('%Y-%m-%d')
    end_date = pd.to_datetime('2023-12-31').strftime('%Y-%m-%d')
    registrations = pd.read_sql_query(
        f"SELECT COUNT(*) FROM project_db WHERE Дата_регистрации BETWEEN '{start_date}' AND '{end_date}'", connection)
    print("Б:")
    print(registrations.iloc[0, 0])


    date = pd.to_datetime('now').strftime('%Y-%m-%d')
    users_years = pd.read_sql_query(
        f"SELECT * FROM project_db WHERE (strftime('%Y', '{date}') - strftime('%Y', Дата_рождения)) BETWEEN 18 AND 35", connection)

    print("В:")
    print(users_years)
