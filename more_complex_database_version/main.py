import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import aiosqlite
import asyncio

fake = Faker('ru_RU')


max_records = 1000000


data = {
    'id': np.arange(1, max_records + 1),
    'ФИО': [fake.name() for _ in range(max_records)],
    'Дата_рождения': [fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d') for _ in range(max_records)],
    'номер_телефона': [fake.phone_number() for _ in range(max_records)],
    'регион': [fake.region() for _ in range(max_records)],
    'Дата_регистрации': [fake.date_this_decade().strftime('%Y-%m-%d') for _ in range(max_records)],
    'курс_обучения': [fake.random_int(1, 5) for _ in range(max_records)],
    'вуз': [fake.company() for _ in range(max_records)]
}


df = pd.DataFrame(data)


df['Дата_рождения'] = pd.to_datetime(df['Дата_рождения'])
df['Дата_регистрации'] = pd.to_datetime(df['Дата_регистрации'])


engine = create_engine('sqlite:///project_database', echo=False)
df.to_sql('database', con=engine, if_exists='append', index=False)
