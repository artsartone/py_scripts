import requests
from yandex_tracker_client import TrackerClient
import logging

client = TrackerClient(iam_token="t1.9euelZqYnsiLlonLkJ3NzpWJyZjIm-3rnpWakIvJkoyQxsidkIyZzouLy57l8_cvdiZC-e9kPx0Y_t3z928kJEL572Q_HRj-zef1656VmpuelpGOlo_Nz5ObzI2cl5nL7_zF656VmpuelpGOlo_Nz5ObzI2cl5nL.Mw_zekbsvGdjmbLApeXItni_u8yNPWKjaJybboqcBOAL3VLzEOuu9oc5CPOocILbWf8r0swqdJDwil304kpCAg", cloud_org_id="bpfbu7h2q3i8e83avh49")

def find_and_print_issues(YEAR, QUEUE_KEY):
    # Формируем фильтр
    date_filter = f'Created: "{YEAR}-01-01 00:00:00".."{YEAR}-12-31 23:59:59" Queue: {QUEUE_KEY}'

    try:
        # Используем метод find для поиска задач
        issues = client.issues.find(query=date_filter)

        # Вывод результатов
        for issue in issues:
            logging.info(f"Задача: {issue.key}, создана: {issue.createdAt}")
    except Exception as e:
        logging.error(f"Ошибка при поиске задач: {e}")

# Пример вызова функции
find_and_print_issues(2025, "test_workflow")