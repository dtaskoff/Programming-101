import requests
import config
import zipfile


def request(url):
    return requests.get(url, auth=(config._USER, config._PASS))

def get_repos_url(user):
    url = "https://api.github.com/users/{0}".format(user)
    r = request(url)
    repos_url = r.json()["repos_url"]

    return repos_url

def fetch_repos(user):
    repos_url = get_repos_url(user)
    r = request(repos_url)
    repos = r.json()
    list_of_repos = [repo["name"] for repo in repos]

    return list_of_repos

def extract(request, repo):
    file_ = open("{}.zip".format(repo), "wb")
    for chunk in request.iter_content():
        file_.write(chunk)
    file_.close()

def download_repos(user):
    repos = fetch_repos(user)
    url = "https://github.com/%s/{}/archive/master.zip" % (user)

    for repo in repos:
        r = request(url.format(repo))
        extract(r, repo)

def lines_of_code(repo):
    pass

def get_stat_for_repo(zip_file):
    pass

def main():
    download_repos("dtaskoff")


if __name__ == '__main__':
    main()