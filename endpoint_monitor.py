import time
from config_parser import read_config
from endpoint_health_checker import check_health
from urllib.parse import urlparse

def calculate_availability(stats):
    return (stats['up'] / stats['total']) * 100 if stats['total'] > 0 else 0

def print_availability(results):
    for domain, stats in results.items():
        availability = calculate_availability(stats)
        print(f"{domain} Availability: {availability:.0f}%")

def monitor_endpoints(config):
    results = {}

    for endpoint in config:
        domain = urlparse(endpoint['url']).netloc
        if domain not in results:
            results[domain] = {'up': 0, 'total': 0}

    try:
        while True:
            for endpoint in config:
                domain = urlparse(endpoint['url']).netloc
                is_up = check_health(endpoint)
                results[domain]['total'] += 1
                if is_up:
                    results[domain]['up'] += 1

            print_availability(results)

            time.sleep(15)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

def main(file_path):
    config = read_config(file_path)
    monitor_endpoints(config)

if __name__ == "__main__":
    main("config.yaml")