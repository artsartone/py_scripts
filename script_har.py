import json

try:
    # Загрузка HAR файла
    with open(r'D:\py_scripts\tracker.yandex.ru.txt', 'r', encoding='utf-8') as f:
        har_data = json.load(f)


    # Функция для поиска ошибок в HAR файле
    def find_errors(har_data):
        errors = []
        for entry in har_data['log']['entries']:
            request_url = entry['request']['url']
            response_status = entry['response']['status']
            response_time = entry['time']

            if 400 <= response_status < 600:
                errors.append({
                    'url': request_url,
                    'status': response_status,
                    'time': response_time,
                    'request_headers': entry['request']['headers'],
                    'response_headers': entry['response']['headers'],
                    'request_method': entry['request']['method'],
                    'response_body': entry['response'].get('content', {}).get('text', '')
                })

        return errors


    # Найти и вывести ошибки
    errors = find_errors(har_data)
    for error in errors:
        print(f"URL: {error['url']}")
        print(f"Status: {error['status']}")
        print(f"Time: {error['time']} ms")
        print(f"Request Method: {error['request_method']}")
        print("Request Headers:")
        for header in error['request_headers']:
            print(f"  {header['name']}: {header['value']}")
        print("Response Headers:")
        for header in error['response_headers']:
            print(f"  {header['name']}: {header['value']}")
        print("Response Body:")
        print(error['response_body'])
        print("")

    # Вывод общего числа ошибок
    print(f"Total errors found: {len(errors)}")
except FileNotFoundError as e:
    print(f"Error: {e}")