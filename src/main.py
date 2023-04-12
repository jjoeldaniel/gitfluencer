from github import Github
from dotenv import load_dotenv
import os

# Create API object from token
load_dotenv()
api_token = os.getenv("API_TOKEN")
git = Github(api_token)

# Build set of followers for the primary user
followers = set()
for data in git.get_user().get_followers().get_page(0):
    followers.add(data)

# Compare to list of following
print('List of non-followers\n=====================')
for user in git.get_user().get_following().get_page(0):

    # If a user is in this following list but is not
    # following the primary user, then we can conclude
    # that this is not a mutual follow.

    # Print GitHub username and name (if set)
    if user not in followers:
        print(f'Username: {user.login}')
        if user.name is not None:
            print(f'Name: {user.name}')
        print()
