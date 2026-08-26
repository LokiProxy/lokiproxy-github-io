const https = require("https");
const { HttpsProxyAgent } = require("https-proxy-agent");


function requiredEnv(name) {
    const value = process.env[name];

    if (!value) {
        console.error(
            `Missing required environment variable: ${name}`
        );

        process.exit(1);
    }

    return value;
}


const host = requiredEnv("LOKIPROXY_HOST");
const port = requiredEnv("LOKIPROXY_PORT");
const username = requiredEnv("LOKIPROXY_USERNAME");
const password = requiredEnv("LOKIPROXY_PASSWORD");


const proxyURL =
    `http://${encodeURIComponent(username)}:` +
    `${encodeURIComponent(password)}@` +
    `${host}:${port}`;


const proxyAgent = new HttpsProxyAgent(proxyURL);


const targetURL = "https://example.com/";


https.get(
    targetURL,
    {
        agent: proxyAgent,

        headers: {
            "User-Agent": "LokiProxy-Example/1.0"
        }
    },

    (response) => {
        let body = "";

        response.on("data", (chunk) => {
            body += chunk;
        });

        response.on("end", () => {
            console.log("Request succeeded.");
            console.log(
                "Status code:",
                response.statusCode
            );

            console.log("Target URL:", targetURL);

            console.log("\nResponse preview:");
            console.log(body.substring(0, 500));
        });
    }
).on("error", (error) => {
    console.error(
        "Request failed:",
        error.message
    );

    process.exit(1);
});
