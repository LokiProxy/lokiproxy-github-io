# LokiProxy - Proxy Service

LokiProxy provides developer-friendly proxy infrastructure and integration examples for HTTP and SOCKS5 proxy connections.

### Features

- HTTP proxy support
- SOCKS5 proxy support
- Username/password authentication
- IP whitelist authentication
- Rotating proxy support
- Sticky session support
- Python integration examples
- Go integration examples
- Node.js integration examples
- Developer-focused documentation

### Quick Start

#### Installation

For Python HTTP proxy support:

```bash
pip install requests
```

For Python SOCKS5 support:

```bash
pip install "requests[socks]"
```

For Go, the examples use the standard library.

For Node.js:

```bash
npm install axios
```

#### Basic Usage

A typical HTTP proxy URL uses the following format:

```text
http://USERNAME:PASSWORD@HOST:PORT
```

Example in Python:

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

Example with SOCKS5:

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

### Proxy Configuration

Replace the following placeholders with your LokiProxy proxy configuration:

- `USERNAME` — proxy username
- `PASSWORD` — proxy password
- `HOST` — proxy hostname or IP address
- `PORT` — proxy port

Example HTTP proxy:

```text
http://USERNAME:PASSWORD@HOST:PORT
```

Example SOCKS5 proxy:

```text
socks5h://USERNAME:PASSWORD@HOST:PORT
```

Do not publish real proxy credentials in source code or documentation.

### Using Environment Variables

For production applications, avoid hard-coding proxy credentials in source code.

Set the following environment variables:

```bash
export LOKIPROXY_HOST="HOST"
export LOKIPROXY_PORT="PORT"
export LOKIPROXY_USERNAME="USERNAME"
export LOKIPROXY_PASSWORD="PASSWORD"
```

Then use them in Python:

```python
import os
import requests

host = os.environ["LOKIPROXY_HOST"]
port = os.environ["LOKIPROXY_PORT"]
username = os.environ["LOKIPROXY_USERNAME"]
password = os.environ["LOKIPROXY_PASSWORD"]

proxy = f"http://{username}:{password}@{host}:{port}"

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

### Documentation

- [Proxy Types](docs/proxy-types.md)
- [Authentication](docs/authentication.md)
- [API Reference](docs/api.md)

### Examples

- [Python HTTP Proxy](examples/python/)
- [Go Integration](examples/go/)
- [Node.js Integration](examples/nodejs/)

### FAQ

#### Which proxy protocols are supported?

LokiProxy supports HTTP and SOCKS5 proxy connections.

#### How do I configure an HTTP proxy?

Use the following format:

```text
http://USERNAME:PASSWORD@HOST:PORT
```

#### How do I configure a SOCKS5 proxy?

Use the following format:

```text
socks5h://USERNAME:PASSWORD@HOST:PORT
```

Python SOCKS5 support requires:

```bash
pip install "requests[socks]"
```

#### Should I commit proxy credentials to GitHub?

No. Never commit real proxy usernames, passwords, API keys, or other secrets to a public repository.

Use environment variables or another secure secrets-management solution instead.

### Contributing

Contributions are welcome.

Before submitting a pull request:

1. Keep examples runnable.
2. Do not include real proxy credentials.
3. Test code examples before submitting changes.
4. Update documentation when configuration or behavior changes.
5. Keep documentation focused on legitimate technical use cases.

### License

See the repository license for licensing information.
