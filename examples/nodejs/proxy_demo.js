const axios = require("axios");
const { SocksProxyAgent } = require("socks-proxy-agent");

const username = process.env.LOKIPROXY_USERNAME || "USERNAME";
const password = process.env.LOKIPROXY_PASSWORD || "PASSWORD";
const host = process.env.LOKIPROXY_HOST || "HOST";
const port = process.env.LOKIPROXY_PORT || "PORT";

async function httpProxyExample() {
  const response = await axios.get("http://example.com/", {
    proxy: {
      protocol: "http",
      host: host,
      port: Number(port),
      auth: {
        username: username,
        password: password,
      },
    },
    timeout: 30000,
  });

  console.log("HTTP proxy status:", response.status);
}

async function socks5ProxyExample() {
  const proxyUrl =
    `socks5h://${encodeURIComponent(username)}:` +
    `${encodeURIComponent(password)}@${host}:${port}`;

  const agent = new SocksProxyAgent(proxyUrl);

  const response = await axios.get("http://example.com/", {
    httpAgent: agent,
    proxy: false,
    timeout: 30000,
  });

  console.log("SOCKS5 proxy status:", response.status);
}

async function main() {
  await httpProxyExample();
  await socks5ProxyExample();
}

main().catch((error) => {
  console.error("Request failed:", error.message);
});
