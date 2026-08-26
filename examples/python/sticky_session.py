import os
import time
import requests


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )

    return value


def build_proxy_url() -> str:
    host = get_required_env("LOKIPROXY_HOST")
    port = get_required_env("LOKIPROXY_PORT")
    username = get_required_env("LOKIPROXY_USERNAME")
    password = get_required_env("LOKIPROXY_PASSWORD")

    return (
        f"http://{username}:{password}"
        f"@{host}:{port}"
    )


def main() -> None:
    proxy_url = build_proxy_url()

    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    target_url = "https://example.com/"

    print("Starting sticky-session example.")
    print("The proxy configuration should be configured")
    print("as Sticky IP in the LokiProxy dashboard.")
    print()

    for request_number in range(1, 4):
        response = requests.get(
            target_url,
            proxies=proxies,
            timeout=30,
            headers={
                "User-Agent": "LokiProxy-Example/1.0"
            },
        )

        response.raise_for_status()

        print(
            f"Request #{request_number}: "
            f"HTTP {response.status_code}"
        )

        time.sleep(2)


if __name__ == "__main__":
    main()
