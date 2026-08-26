# Proxy Types

LokiProxy provides proxy connections through HTTP and SOCKS5.

This document explains the supported proxy connection formats and how to configure them in applications.

## HTTP Proxy

HTTP proxies use the following format:

```text
http://USERNAME:PASSWORD@HOST:PORT
```

Where:

- `USERNAME` is your proxy username.
- `PASSWORD` is your proxy password.
- `HOST` is the proxy hostname or IP address.
- `PORT` is the proxy port.

### Python Example

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

print(response.status_code)
```

## SOCKS5 Proxy

SOCKS5 proxies use the following format:

```text
socks5h://USERNAME:PASSWORD@HOST:PORT
```

The `socks5h` scheme allows hostname resolution to be performed through the SOCKS5 proxy.

### Python Installation

Install SOCKS5 support for Requests:

```bash
pip install "requests[socks]"
```

### Python Example

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

print(response.status_code)
```

## Comparison

| Feature | HTTP | SOCKS5 |
|---|---|---|
| Proxy scheme | `http://` | `socks5h://` |
| Username/password | Supported | Supported |
| Python Requests | Supported | Supported with `requests[socks]` |
| Typical use | HTTP client applications | Applications requiring SOCKS5 support |

## Security

Do not publish real proxy credentials in source code.

Use placeholders in documentation:

```text
USERNAME
PASSWORD
HOST
PORT
```

For production applications, load credentials from environment variables or a secure secrets-management system.
