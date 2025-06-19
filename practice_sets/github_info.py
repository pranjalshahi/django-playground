import requests
r = requests.get("https://api.github.com/users/pranjalshahi").json()
r.raise_for_status()
print(r.get("login"), "   ", r.get("organizations_url"))