import requests
r = requests.get("https://api.github.com/users/pranjalshahi")
r.raise_for_status()

print(r.json().get("login"), "   ", r.json().get("organizations_url"))