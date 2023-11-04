### Configuration
# Logging Options

import os


LOG = True
LOG_FILE = os.path.join("D:\\Creations\\GithubCommit\\Commit-Bot-main", "GeometricAnalysis.log")

# Commit Options
NO_COMMIT_CHANCE = 0.1 # 10% chance of NOT committing to GitHub.
MAX_COMMITS = 80 # Maximum number of commits that can be made.

# Cron job.
#CRON_JOB_TIME = "0 12 * * *" # Every day at 12:00 pm.


# Output File
OUTPUT_FILE = os.path.join("D:\\Creations\\GithubCommit\\Commit-Bot-main", "FactorAnalysis.txt")



# Imports
from random import choice
from sys import argv
from pathlib import Path
from os import system # Executing the Git commands.
from random import random, randint # Generating a random float between 0 and 1.
from datetime import datetime # Date and time for our file.
# Set the working directory to the directory where your Git repository is located
os.chdir("D:\\Creations\\GithubCommit\\Commit-Bot-main")

# # Check if a cronjob exists for this script, if not, create it using crontab.
# system("crontab -l > cron.txt")
# with open("cron.txt", "r") as f:
#     if "commit_bot.py" not in f.read():
#         with open("cron.txt", "a") as f:
#             f.write(f"{CRON_JOB_TIME} cd {Path.cwd()} && python3 commit_bot.py\n")
#             f.close()
#             system("crontab cron.txt")
#             system("rm -f cron.txt")
#     else:
#         f.close()
#         system("rm -f cron.txt")

# Logging.
def log(message):
    if LOG:
        with open(LOG_FILE, "a") as f:
            f.write(f"{message}\n")
            f.close()


commit_messages = [
    "Implemented a new feature: hyperparameter tuning using GridSearchCV.",
    "Updated data preprocessing pipeline for improved accuracy.",
    "Refactored code for better readability and maintainability.",
    "Resolved merge conflicts with the latest master branch.",
    "Added data visualization for model evaluation.",
    "Fixed a bug in the cross-validation code.",
    "Implemented early stopping to prevent overfitting.",
    "Added unit tests for data preprocessing functions.",
    "Optimized model training with parallel processing.",
    "Fixed compatibility issues with Python 3.8.",
    "Resolved merge conflicts with the latest master branch.",
    "Updated data preprocessing pipeline for improved accuracy.",
    "Improved model interpretability with SHAP values.",
    "Added support for GPU acceleration in model training.",
    "Updated project dependencies to address security vulnerabilities."
]



# Create our commit.
def create_commit():
    with open(OUTPUT_FILE, "w") as f:
        f.write(str(datetime.now()))
        f.close()
    random_message = choice(commit_messages)

    system(f"git add .")
    system(f"git commit -m \"{random_message}\"")

# Execute the script.
if (random() > NO_COMMIT_CHANCE):
    CommitCountinput = int(input("Enter commit count: "))
    commits = randint(0, MAX_COMMITS)
    if CommitCountinput != 0:
        commits = CommitCountinput

    for i in range(commits):
        create_commit()
    system("git push")
    log(f"[{datetime.now()}] Sucessfully committed {commits} time(s).")
else:
    log(f"[{datetime.now()}] No commits were made.")
