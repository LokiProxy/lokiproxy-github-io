const axios = require("axios");

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

  console.log("Status:", response.status);
}

httpProxyExample().catch((error) => {
  console.error("Request failed:", error.message);
});
