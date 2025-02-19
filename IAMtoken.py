import requests
from yandex_tracker_client import TrackerClient
import logging

# Ваши данные
OAUTH_TOKEN = ""
ORG_ID = ""


logging.basicConfig(level=logging.INFO)

# Функция для получения IAM-токена
def get_iam_token(oauth_token):
    response = requests.post(
        "https://iam.api.cloud.yandex.net/iam/v1/tokens",
        json={"yandexPassportOauthToken": oauth_token},
    )
    if response.status_code == 200:
        return response.json().get("iamToken")
    else:
        raise Exception(
            f"Error getting IAM token: {response.status_code}, {response.text}"
        )


# Получаем IAM-токен
IAM_TOKEN = get_iam_token(OAUTH_TOKEN)

# Инициализация клиента Tracker с IAM-токеном
client = TrackerClient(iam_token=IAM_TOKEN, cloud_org_id=ORG_ID)

#print(IAM_TOKEN)

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