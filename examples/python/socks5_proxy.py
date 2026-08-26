import os
import requests


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )

    return value


def build_socks5_proxy_url() -> str:
    host = get_required_env("LOKIPROXY_SOCKS5_HOST")
    port = get_required_env("LOKIPROXY_SOCKS5_PORT")
    username = get_required_env("LOKIPROXY_USERNAME")
    password = get_required_env("LOKIPROXY_PASSWORD")

    return (
        f"socks5h://{username}:{password}"
        f"@{host}:{port}"
    )


def main() -> None:
    proxy_url = build_socks5_proxy_url()

    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    target_url = "https://example.com/"

    response = requests.get(
        target_url,
        proxies=proxies,
        timeout=30,
        headers={
            "User-Agent": "LokiProxy-Example/1.0"
        },
    )

    response.raise_for_status()

    print("SOCKS5 request succeeded.")
    print("Status code:", response.status_code)
    print("Target URL:", target_url)

    print("\nResponse preview:")
    print(response.text[:500])


if __name__ == "__main__":
    main()
