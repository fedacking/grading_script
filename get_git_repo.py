import os
import subprocess

def get_repo_gh(url, branch=None, folder="input"):
    user = url.split(":")[1].split('/')[-2]
    name = url.split(":")[1].split('/')[-1]

    # We check the folder for the user, we create it
    user_folder = os.path.join(folder, user)
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)

    # We check if the repo exists
    repo_folder = user_folder + '/' + name

    # We download if it does
    if not os.path.exists(repo_folder) or len(os.listdir(repo_folder)) == 0:
        subprocess.run(["git", "clone", url, repo_folder], capture_output=True)

    # We update if it does not
    else:
        subprocess.run(["git", "pull"], cwd=repo_folder, capture_output=True)
    

    # If branch, we go to that branch
    if branch != None:
        subprocess.run(["git", "checkout", branch], cwd=repo_folder, capture_output=True)

    return repo_folder