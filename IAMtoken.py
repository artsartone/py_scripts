import requests
from yandex_tracker_client import TrackerClient

# Ваши данные
OAUTH_TOKEN = 'y0__xDX8rD7AxizmDUg6ZT-oBKvyFI_hiwaAHNj78r96z2XWjIt1w'
X_ORG_ID = 'bpfbu7h2q3i8e83avh49'  # Убедитесь, что это строка

# Функция для получения IAM-токена
def get_iam_token(oauth_token):
    response = requests.post(
        'https://iam.api.cloud.yandex.net/iam/v1/tokens',
        json={"yandexPassportOauthToken": oauth_token}
    )
    if response.status_code == 200:
        return response.json().get('iamToken')
    else:
        raise Exception(f"Error getting IAM token: {response.status_code}, {response.text}")

# Получаем IAM-токен
IAM_TOKEN = get_iam_token(OAUTH_TOKEN)

# Инициализация клиента Tracker с IAM-токеном
client = TrackerClient(token=IAM_TOKEN, cloud_org_id=X_ORG_ID)

# Пример использования клиента
issues = client.issues.get_all()
for issue in issues:
    print(issue.key)