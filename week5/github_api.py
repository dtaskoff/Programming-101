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

def fetch_repos(repos_url):
    r = request(repos_url)
    repos = r.json()
    list_of_repos = [repo["name"] for repo in repos]

    return list_of_repos

def save_to_disk(request, repo):
    file_ = open("{}.zip".format(repo), "wb")
    for chunk in request.iter_content():
        file_.write(chunk)
    file_.close()

def download_repos(repos_names, user):
    url = "https://github.com/%s/{}/archive/master.zip" % (user)

    for repo in repos_names:
        r = request(url.format(repo))
        save_to_disk(r, repo)

def unzip_repos(repos_names):
    for repo in repos_names:
        with zipfile.ZipFile("{}.zip".format(repo)) as myzip:
            myzip.extractall()

def get_repos_stats(repos_names):
    pass

def main():
    # user = "dtaskoff"
    # repos_url = get_repos_url("user")
    # repos_names = fetch_repos(repos_url)
    # download_repos(repos_names, "user")
    # unzip_repos(repos_names)
    # get_repos_stats(repos_names)
    pass


if __name__ == '__main__':
    main()