package main

import (
	"fmt"
	"net/http"
	"net/url"
	"os"
)

func main() {
	username := os.Getenv("LOKIPROXY_USERNAME")
	password := os.Getenv("LOKIPROXY_PASSWORD")
	host := os.Getenv("LOKIPROXY_HOST")
	port := os.Getenv("LOKIPROXY_PORT")

	if username == "" {
		username = "USERNAME"
	}

	if password == "" {
		password = "PASSWORD"
	}

	if host == "" {
		host = "HOST"
	}

	if port == "" {
		port = "PORT"
	}

	proxyURL := &url.URL{
		Scheme: "http",
		Host:   host + ":" + port,
	}

	proxyURL.User = url.UserPassword(username, password)

	client := &http.Client{
		Transport: &http.Transport{
			Proxy: http.ProxyURL(proxyURL),
		},
	}

	response, err := client.Get("http://example.com/")
	if err != nil {
		fmt.Println("Request failed:", err)
		return
	}

	defer response.Body.Close()

	fmt.Println("Status:", response.Status)
}
