import requests

def enumerate_subdomains(domain):
    """
    Enumerate subdomains of a given domain using the SecurityTrails API.
    Ensure you have obtained an API key and have permission to enumerate the target domain.
    """
    API_KEY = 'ca-wnB8IXtfYYCSWhPkfzcxBqPaYr3Vp'
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {
        'APIKEY': API_KEY,
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            subdomains = response.json()['subdomains']
            for subdomain in subdomains:
                print(f"{subdomain}.{domain}")
        else:
            print("Failed to retrieve subdomains. Ensure your API key is valid and you have permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain you want to enumerate subdomains for: ")
    enumerate_subdomains(domain)
