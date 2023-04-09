import pygit2
import os
import subprocess

def get_repo_gh(url, branch=None, folder="input"):
    user = url.split('/')[-2]
    name = url.split('/')[-1]

    # We check the folder for the user, we create it
    user_folder = os.path.join(folder, user)
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)

    # We check if the repo exists
    repo_folder = user_folder + '/' + name

    # We download if it does
    if not os.path.exists(repo_folder) or len(os.listdir(repo_folder)) == 0:
        subprocess.run(["git", "clone", url, repo_folder])

    # We update if it does not
    else:
        subprocess.run(["git", "pull"], cwd=repo_folder)
    

    # If branch, we go to that branch
    if branch != None:
        subprocess.run(["git", "checkout", branch], cwd=repo_folder)

    return repo_folder