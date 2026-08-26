import os
import requests


def build_proxy_url():
    username = os.getenv("LOKIPROXY_USERNAME", "USERNAME")
    password = os.getenv("LOKIPROXY_PASSWORD", "PASSWORD")
    host = os.getenv("LOKIPROXY_HOST", "HOST")
    port = os.getenv("LOKIPROXY_PORT", "PORT")

    return f"http://{username}:{password}@{host}:{port}"


def main():
    proxy = build_proxy_url()

    proxies = {
        "http": proxy,
    }

    session = requests.Session()

    session.proxies.update(proxies)

    urls = [
        "http://example.com/",
        "http://example.com/",
        "http://example.com/",
    ]

    for url in urls:
        response = session.get(
            url,
            timeout=30,
        )

        response.raise_for_status()

        print(
            "Status:",
            response.status_code,
            "URL:",
            response.url,
        )


if __name__ == "__main__":
    main()
