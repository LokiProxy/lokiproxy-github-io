import os
import requests


def build_proxy_url():
    username = os.getenv("LOKIPROXY_USERNAME", "USERNAME")
    password = os.getenv("LOKIPROXY_PASSWORD", "PASSWORD")
    host = os.getenv("LOKIPROXY_HOST", "HOST")
    port = os.getenv("LOKIPROXY_PORT", "PORT")

    return f"socks5h://{username}:{password}@{host}:{port}"


def main():
    proxy = build_proxy_url()

    proxies = {
        "http": proxy,
    }

    response = requests.get(
        "http://example.com/",
        proxies=proxies,
        timeout=30,
    )

    response.raise_for_status()

    print("Status:", response.status_code)
    print("Final URL:", response.url)


if __name__ == "__main__":
    main()
