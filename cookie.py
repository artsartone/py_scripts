import json
import pandas as pd

# Функция для загрузки HAR файла
def load_har(file_path):
    with open(r'D:\py_scripts\tracker.yandex.ru.txt', 'r', encoding='utf-8') as file:
        har_data = json.load(file)
    return har_data

# Функция для извлечения информации из HAR файла
def extract_info(har_data):
    entries = har_data['log']['entries']
    records = []

    for entry in entries:
        request = entry['request']
        response = entry['response']

        record = {
            'url': request['url'],
            'method': request['method'],
            'request_headers': request.get('headers', []),
            'request_cookies': request.get('cookies', []),
            'request_body': request.get('postData', {}).get('text', ''),
            'response_status': response['status'],
            'response_headers': response.get('headers', []),
            'response_cookies': response.get('cookies', []),
            'response_body': response.get('content', {}).get('text', '')
        }
        records.append(record)

    return pd.DataFrame(records)

# Основная часть программы
har_file_path = 'path_to_your_file.har'  # Укажите путь к вашему HAR файлу
har_data = load_har(har_file_path)
df = extract_info(har_data)

# Сохранение результатов в CSV файл для дальнейшего анализа
df.to_csv('har_analysis.csv', index=False)

# Печать первых 5 записей для проверки
print(df.head())