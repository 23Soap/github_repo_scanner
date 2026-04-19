import requests
while True:
    print("Enter Github Username")
    username = input()
    print("Username:" + username)

    git_hub_url = f"https://api.github.com/users/{username}/repos"
    r = requests.get(git_hub_url, headers={"Accept": "application/json"})
    #print(f"status code{r.status_code} , Context: {r.json()}")
    repos = r.json()
    if r.status_code != 200:
        print("Github Username Not Found")
        continue
    # print(repos)
    for repo in repos:
        print(repo['name'])
    print("Enter Repository Name")
    repo_name = input()
    print("Selected Branch")
    branch_name = input()

    branch_url = f"https://api.github.com/repos/{username}/{repo_name}/git/trees/{branch_name}?recursive=1"
    g = requests.get(branch_url, headers={"Accept": "application/json"})
    # print(f"status code{g.status_code} , Context: {g.json()}")
    tree = g.json()
    # print(tree)
    for items in tree["tree"]:
        print(items['path'])
        print(f"https://raw.githubusercontent.com/{username}/{repo_name}/{branch_name}/{items['path']}")


    while True:
     cont = input("Do you want to continue (y/n)?")
     if cont == "y":
        break
     elif cont == "n":
        break
     else:
        print("Enter Y or N")
    if cont == "n":
        break

