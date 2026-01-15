!ls /repos

import os
token = os.environ["GITHUB_TOKEN"]

import os
from git import Repo

username = "user01"
file = "AI_Modeler_Demo_01.py"

token = os.getenv("GITHUB_TOKEN")

url = f"https://x-access-token:{token}@github.com/aimodeler-demo/{username}.git"
repo_dir = f"/repos/{username}"


if not os.path.exists(repo_dir):
    # Clone if folder doesn't exist
    repo = Repo.clone_from(url, repo_dir)
else:
    # Open existing repo
    repo = Repo(repo_dir)


file_path = os.path.join(repo_dir, file)

# ✅ Copy your existing AI_Modeler_Demo.py into the repo before pushing
import shutil
shutil.copy(file, file_path)

# Then push it
repo.git.add(all=True)
repo.index.commit("Auto-update: AI model")
repo.remote(name="origin").set_url(f"https://x-access-token:{token}@github.com/aimodeler-demo/{username}.git")
repo.remote(name="origin").push()