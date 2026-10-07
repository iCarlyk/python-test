import requests


def main():
    response = requests.get("https://example.com", timeout=10)
    print(f"HTTP status: {response.status_code}")
    print(f"Content length: {len(response.text)} bytes")


if __name__ == "__main__":
    main()
