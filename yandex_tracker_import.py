from yandex_tracker_client import TrackerClient
from datetime import datetime

client = TrackerClient(token='', cloud_org_id='')


import pandas as pd
import numpy as np

df = pd.read_excel(r'D:\py_scripts non git\tracker.xlsx')

# for i, row in df.iterrows():
#     print(f"Index: {i}")
#     print(f"{row['Задача']}")
#     print(f"{row['Исполнитель']}")
#     print(f"{row['Автор']}")
#     print(f"{row['Статус']}")
#     print(f"{row['Обновлено']}")
#     print(f"{row['Создано']}")
#     print(f"{row['Дата завершения']}")
#     print(f"{row['Тип']}")
#     print(f"{row['Компания']}")

for i, row in df.iterrows():

    try:
        end = row['Дата завершения'].strftime("%Y-%m-%d")
    except Exception as e:
        end = ""

    issue = client.issues.import_object(
        queue='TESTWORKFLOW',
        summary=row['Задача'],
        type=row['Тип'],
        assignee=row['Исполнитель'],
        author=row['Автор'],
        status=row['Статус'],
        globalTextField=row['Компания'],
        createdAt=row['Создано'].strftime("%Y-%m-%d"),
        end=end
    )