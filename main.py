from datetime import datetime, timedelta
import subprocess

def create_commit(date: datetime):
    dateStr = date.strftime("%a %b %d %I:%M %Y +0700")
    with open("out.txt", "a") as f:
        f.write("a")
    subprocess.run(["git", "add", "test.txt"])
    subprocess.run(["git", "commit", "-m", "commit",])
    subprocess.run(["git", "commit", "--amend", "-m", "commit", f'--date="{dateStr}"',])
    
def create_commits_for_date(numCommits: int, date: datetime):
    dateStr = date.strftime("%a %b %d %I:%M %Y +0700")
    print(f"Creating {numCommits} on {dateStr}")
    for _ in range(numCommits):
        create_commit(date)


def get_commit_date(startDate, weeks, day):
    return startDate + timedelta(weeks=weeks, days=day)

if __name__ == "__main__":
    commit_date = datetime.today() - timedelta(weeks=1, days=0)

    num_commits = 1

    print(f"Commit date: {commit_date.strftime('%m-%d-%Y')}, commits: {num_commits}")
    create_commits_for_date(num_commits, commit_date)