import requests

print("Enter Github Username")
username = input()
print("Username:" + username)

git_hub_url = f"https://api.github.com/users/{username}/repos"
r = requests.get(git_hub_url,headers = {"Accept" : "application/json"})
print(f"status code{r.status_code} , Context: {r.json()}")
repos = r.json()
for repo in repos:
    print(repo["name"])