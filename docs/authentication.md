# Authentication

LokiProxy proxy connections can use username/password authentication.

## Username and Password

The standard proxy URL format is:

```text
http://USERNAME:PASSWORD@HOST:PORT
```

For SOCKS5:

```text
socks5h://USERNAME:PASSWORD@HOST:PORT
```

Replace the placeholders with the credentials provided by your proxy configuration.

## Authentication Parameters

| Parameter | Description |
|---|---|
| `USERNAME` | Proxy username |
| `PASSWORD` | Proxy password |
| `HOST` | Proxy hostname or IP address |
| `PORT` | Proxy service port |

## HTTP Example

```python
import requests

proxy = "http://USERNAME:PASSWORD@HOST:PORT"

proxies = {
    "http": proxy,
}

response = requests.get(
    "http://example.com/",
    proxies=proxies,
    timeout=30,
)

response.raise_for_status()

print(response.status_code)
```

## SOCKS5 Example

Install the required Python dependency:

```bash
pip install "requests[socks]"
```

Then configure the SOCKS5 proxy:

```python
import requests

proxy = "socks5h://USERNAME:PASSWORD@HOST:PORT"

proxies = {
    "http": proxy,
}

response = requests.get(
    "http://example.com/",
    proxies=proxies,
    timeout=30,
)

response.raise_for_status()

print(response.status_code)
```

## Environment Variables

Credentials should not normally be stored directly in source code.

Set the following environment variables:

```bash
export LOKIPROXY_USERNAME="USERNAME"
export LOKIPROXY_PASSWORD="PASSWORD"
export LOKIPROXY_HOST="HOST"
export LOKIPROXY_PORT="PORT"
```

Then construct the proxy URL in Python:

```python
import os

username = os.environ["LOKIPROXY_USERNAME"]
password = os.environ["LOKIPROXY_PASSWORD"]
host = os.environ["LOKIPROXY_HOST"]
port = os.environ["LOKIPROXY_PORT"]

proxy = f"http://{username}:{password}@{host}:{port}"

print(proxy)
```

## Credential Safety

Never commit real credentials to GitHub.

Do not put real values into examples such as:

```text
USERNAME
PASSWORD
HOST
PORT
```

Use placeholders instead.

If a real credential is accidentally committed, revoke or rotate it immediately.

## IP Whitelisting

If your LokiProxy configuration uses IP whitelisting instead of username/password authentication, configure the allowed client IP address through the LokiProxy service configuration.

Do not place private access credentials or internal configuration information in this repository.
