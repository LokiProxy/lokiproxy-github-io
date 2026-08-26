package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
)

func requiredEnv(name string) string {
	value := os.Getenv(name)

	if value == "" {
		fmt.Printf("Missing required environment variable: %s\n", name)
		os.Exit(1)
	}

	return value
}

func main() {
	host := requiredEnv("LOKIPROXY_HOST")
	port := requiredEnv("LOKIPROXY_PORT")
	username := requiredEnv("LOKIPROXY_USERNAME")
	password := requiredEnv("LOKIPROXY_PASSWORD")

	proxyURL := &url.URL{
		Scheme: "http",
		Host:   host + ":" + port,
		User:   url.UserPassword(username, password),
	}

	transport := &http.Transport{
		Proxy: http.ProxyURL(proxyURL),
	}

	client := &http.Client{
		Transport: transport,
	}

	targetURL := "https://example.com/"

	request, err := http.NewRequest(
		http.MethodGet,
		targetURL,
		nil,
	)

	if err != nil {
		fmt.Println("Failed to create request:", err)
		os.Exit(1)
	}

	request.Header.Set(
		"User-Agent",
		"LokiProxy-Example/1.0",
	)

	response, err := client.Do(request)

	if err != nil {
		fmt.Println("Request failed:", err)
		os.Exit(1)
	}

	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)

	if err != nil {
		fmt.Println("Failed to read response:", err)
		os.Exit(1)
	}

	fmt.Println("Request succeeded.")
	fmt.Println("Status code:", response.StatusCode)
	fmt.Println("Target URL:", targetURL)

	fmt.Println("\nResponse preview:")
	fmt.Println(string(body[:min(500, len(body))]))
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
