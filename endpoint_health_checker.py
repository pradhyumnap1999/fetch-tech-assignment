import requests

def check_health(endpoint):
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers', {}),
            data=endpoint.get('body', ''),
            timeout=0.5  # 500 ms timeout
        )
        return response.status_code in range(200, 300) and response.elapsed.total_seconds() < 0.5
    except requests.RequestException:
        return False
