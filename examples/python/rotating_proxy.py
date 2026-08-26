import os
import requests


def build_proxy_url():
    username = os.getenv("LOKIPROXY_USERNAME", "USERNAME")
    password = os.getenv("LOKIPROXY_PASSWORD", "PASSWORD")
    host = os.getenv("LOKIPROXY_HOST", "HOST")
    port = os.getenv("LOKIPROXY_PORT", "PORT")

    return f"http://{username}:{password}@{host}:{port}"


def fetch(url):
    proxy = build_proxy_url()

    proxies = {
        "http": proxy,
    }

    response = requests.get(
        url,
        proxies=proxies,
        timeout=30,
    )

    response.raise_for_status()

    return response


if __name__ == "__main__":
    target_url = "http://example.com/"

    response = fetch(target_url)

    print("Status:", response.status_code)
    print("Final URL:", response.url)
