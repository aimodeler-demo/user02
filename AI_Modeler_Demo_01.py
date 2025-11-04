!git clone https://github.com/aimodeler-demo/user01.git /root/repos/user01
%cd /root/repos/user01



!pwd
!ls -a



import os, shutil
from git import Repo

username = "user01"
token = os.getenv("GITHUB_TOKEN")
user = "aimodeler-demo"

repo_dir = f"/repos/{username}"
url = f"https://x-access-token:{token}@github.com/{user}/{username}.git"

# 1️⃣ Delete any old local repo (to avoid merge confusion)
if os.path.exists(repo_dir):
    shutil.rmtree(repo_dir)

# 2️⃣ Reclone fresh from GitHub
repo = Repo.clone_from(url, repo_dir)

# 3️⃣ Copy your updated file in
file = "AI_Modeler_Demo_01.py"
shutil.copy(file, os.path.join(repo_dir, file))

# 4️⃣ Add + commit
repo.git.add(all=True)
repo.index.commit("Force sync: overwrite remote with local changes")

# 5️⃣ Force push (⚠️ overwrites GitHub)
repo.remote("origin").push(force=True)

print("✅ Repo reset and force-pushed successfully.")


import os, shutil
from git import Repo

username = "user01"
token = os.getenv("GITHUB_TOKEN")
user = "aimodeler-demo"

repo_dir = f"/repos/{username}"
file = "AI_Modeler_Demo_01.py"
url = f"https://x-access-token:{token}@github.com/{user}/{username}.git"

# Remove existing repo and reclone fresh
if os.path.exists(repo_dir):
    shutil.rmtree(repo_dir)

repo = Repo.clone_from(url, repo_dir)

# Forcefully overwrite the file
dest_file = os.path.join(repo_dir, file)
if os.path.exists(dest_file):
    os.remove(dest_file)
shutil.copy(file, dest_file)

# Stage and commit
repo.git.add(all=True)
repo.index.commit("Force update: overwrite remote with local AI_Modeler_Demo_01.py")

# Force push to GitHub
repo.remote("origin").push(force=True)

print("✅ Remote file forcibly replaced and pushed.")




!git status
!git add .
!git commit -m "Your commit message"
!git push origin main


import os, shutil
from git import Repo

user = "aimodeler-demo"
repo_name = "user01"
token = os.getenv("GITHUB_TOKEN")

repo_dir = f"/repos/{repo_name}"
url = f"https://x-access-token:{token}@github.com/{user}/{repo_name}.git"

# Delete old local repo if it exists
if os.path.exists(repo_dir):
    shutil.rmtree(repo_dir)

# Reclone fresh from GitHub
Repo.clone_from(url, repo_dir)
print(f"✅ Reset complete: cloned fresh copy to {repo_dir}")_01


print(token)