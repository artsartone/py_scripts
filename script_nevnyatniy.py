from yandex_tracker_client import TrackerClient
from datetime import datetime

# Инициализация клиента Tracker
client = TrackerClient(token='y0__xDX8rD7AxjrsTUgwd39qBJ2-zJojj8Fak4T7h5ly6yVMjF-Fw', cloud_org_id='bpfbu7h2q3i8e83avh49')

# Список статусов, которые мы проверяем
statuses_to_check = 'inProgress'

def fill_academicians_fields(issue):
    print("Функция запущена")
    # Получаем текущую дату в формате YYYY-MM-DD
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Проверяем статус задачи
    if issue.status.key in statuses_to_check:
        print(f"Обнаружен статус '{issue.status.key}' в задаче {issue.key}")

        # Проверяем каждое поле и заполняем, если оно пустое
        dataivremyatest = issue.dataivremyatest  # Поле 1
        dataivremya = issue.dataivremya    # Поле 2

        # Обновляем поля, если они пустые
        if not dataivremyatest:
            issue.update(dataivremyatest=current_date)
        if not dataivremya:
            issue.update(dataivremya=current_date)

def main(event):
    # Извлекаем ID задачи из события (event)
    issue_id = event['queryStringParameters']['id']

    # Получаем задачу по ID
    issue = client.issues[issue_id]

    # Вызываем функцию для заполнения полей
    fill_academicians_fields(issue)

    return {
        'statusCode': 200,
        'body': "Ok"
    }

# Пример вызова функции для локального тестирования
if __name__ == "__main__":
    # Создаем тестовое событие (event)
    test_event = {
        'queryStringParameters': {
            'id': 'PRACTICE-697'  # Замените на реальный ID задачи
        }
    }

    # Вызываем функцию main с тестовым событием
    result = main(test_event)
    print(result)  # Выводим результат выполнения
    
    
    
