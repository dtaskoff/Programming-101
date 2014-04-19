import requests
import config
import zipfile
import os
from collections import defaultdict


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
        zipfile.ZipFile("{}.zip".format(repo)).extractall()

def get_extension(file):
    index = len(file)
    for i in range(len(file)):
        if file[i] == '.':
            index = i
            break
    return file[index:]

def print_extensions(extensions):
    to_print = []
    for extension in extensions:
        to_print.append("\"*{0}\" - {1} files".format(extension,
            extensions[extension]))
    return "\n".join(to_print)

def get_repos_stats(repo):
    extensions = defaultdict(int)
    list_files = os.walk(repo)

    for root, dirs, paths in list_files:
        for path in paths:
            extension = str(get_extension(path))
            extensions[extension] += 1

    return extensions

def get_lines(path):
    file = open(path, "r")
    length = len(file.read().splitlines())
    file.close()

    return length

# TODO
def lines_of_code_in_repo(repo):
    lines = 0
    list_files = os.walk(repo)

    for dirs in list_files:
        dir = dirs[0]
        files = dirs[2]
        for file in files:
            lines += get_lines(dir + '/' + file)

    return "{} lines".format(lines)

def all_repos_stats(repos_names):
    stats = []

    for repo in repos_names:
        repo_full_name = "{}-master".format(repo)
        stats.append(repo)
        stats.append(str(lines_of_code_in_repo(repo_full_name)))
        stats.append(print_extensions(get_repos_stats(repo_full_name)))

    return '\n'.join(stats)


def main():
    user = "dtaskoff"
    repos_url = get_repos_url(user)
    repos_names = fetch_repos(repos_url)
    download_repos(repos_names, user)
    unzip_repos(repos_names)
    print(all_repos_stats(repos_names))


if __name__ == '__main__':
    main()