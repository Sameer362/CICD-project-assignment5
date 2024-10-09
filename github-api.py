import requests
import time

GITHUB_USER = 'sameer362'
REPO_NAME = 'Hello'

API_URL = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/commits'

def get_latest_commit():
    response = requests.get(API_URL)
    if response.status_code == 200:
        commits = response.json()
        return commits[0]['sha'] if commits else None
    else:
        print("Error fetching commits")
        return None

def main():
    last_commit_sha = get_latest_commit()
    print(f"Initial latest commit SHA: {last_commit_sha}")

    while True:
        time.sleep(60)  # Check every 60 seconds
        latest_commit_sha = get_latest_commit()

        if latest_commit_sha != last_commit_sha:
            print(f"New commit detected! SHA: {latest_commit_sha}")
            last_commit_sha = latest_commit_sha
        else:
            print("No new commits.")

if __name__ == "__main__":
    main()

