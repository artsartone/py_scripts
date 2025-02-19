from yandex_tracker_client import TrackerClient

client = TrackerClient(token='y0_AgAAAAA_bDlXAAuQdwAAAAEIHbu4AACJQKPKUa9OTruWzW_UQ_ZKri5cMg', cloud_org_id='bpfbu7h2q3i8e83avh49')

from datetime import datetime
import pandas as pd
import numpy as np

df = pd.read_excel(r'D:\py_sripts\tracker.xlsx')

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
        testPoleTxt=row['Компания'],
        createdAt=row['Создано'].strftime("%Y-%m-%d"),
        end=end
    )