from yandex_tracker_client import TrackerClient
client = TrackerClient(token='', cloud_org_id='')


YEAR = 2025
queue_key = "test_workflow"  # Замените на ключ вашей очереди

# Формируем фильтр
date_filter = f'Created: "{YEAR}-01-01 00:00:00".."{YEAR}-12-31 21:00:00" Queue: {queue_key}'

# Используем метод find для поиска задач
issues = client.issues.find(query=date_filter)

# Вывод результатов
for issue in issues:
    print(f"Задача: {issue.key}, создана: {issue.createdAt}")