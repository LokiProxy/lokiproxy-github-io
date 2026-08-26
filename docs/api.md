# API Reference

This document describes the proxy connection configuration used by the examples in this repository.

## Proxy URL

### HTTP

```text
http://USERNAME:PASSWORD@HOST:PORT
```

Example:

```text
http://USERNAME:PASSWORD@HOST:PORT
```

### SOCKS5

```text
socks5h://USERNAME:PASSWORD@HOST:PORT
```

Example:

```text
socks5h://USERNAME:PASSWORD@HOST:PORT
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `USERNAME` | Yes* | Proxy username |
| `PASSWORD` | Yes* | Proxy password |
| `HOST` | Yes | Proxy hostname or IP address |
| `PORT` | Yes | Proxy port |

`*` Username and password are required when using username/password authentication.

## HTTP Configuration

Python:

```python
proxy = "http://USERNAME:PASSWORD@HOST:PORT"

proxies = {
    "http": proxy,
}
```

## SOCKS5 Configuration

Python:

```python
proxy = "socks5h://USERNAME:PASSWORD@HOST:PORT"

proxies = {
    "http": proxy,
}
```

## Request Timeout

Applications should set a reasonable request timeout.

Example:

```python
response = requests.get(
    "http://example.com/",
    proxies=proxies,
    timeout=30,
)
```

## Environment Variables

Recommended configuration:

```text
LOKIPROXY_USERNAME
LOKIPROXY_PASSWORD
LOKIPROXY_HOST
LOKIPROXY_PORT
```

Example:

```python
import os

username = os.environ["LOKIPROXY_USERNAME"]
password = os.environ["LOKIPROXY_PASSWORD"]
host = os.environ["LOKIPROXY_HOST"]
port = os.environ["LOKIPROXY_PORT"]

proxy = f"http://{username}:{password}@{host}:{port}"
```

## API Management

This repository documents client-side proxy configuration.

Service management API endpoints, API keys, account operations, traffic information, and other account-level APIs should be documented only when the corresponding LokiProxy API specification is available.

Do not invent API endpoints or API credentials in examples.

## Security

Never publish real usernames, passwords, API keys, or other secrets in this repository.
