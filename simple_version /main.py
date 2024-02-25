import pandas as pd
import numpy as np
from faker import Faker


fake = Faker('ru_RU')


max_records = 1000000


data = {
    'id': np.arange(1, max_records + 1),
    'ФИО': [fake.name() for _ in range(max_records)],
    'Дата рождения': [fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d') for _ in range(max_records)],
    'номер телефона': [fake.phone_number() for _ in range(max_records)],
    'регион': [fake.region() for _ in range(max_records)],
    'Дата регистрации': [fake.date_this_decade().strftime('%Y-%m-%d') for _ in range(max_records)],
    'курс обучения': [fake.random_int(1, 5) for _ in range(max_records)],
    'вуз': [fake.company() for _ in range(max_records)]
}


df_itog = pd.DataFrame(data)
