from github import Github
from dotenv import load_dotenv
import os
import requests

# Create API object from token
load_dotenv()
api_token = os.getenv("API_TOKEN")
git = Github(api_token)
to_be_unfollowed = list()


def unfollow_user(target_username: str):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {api_token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }

    response = requests.delete(
        f'https://api.github.com/user/following/{target_username}',
        headers=headers
    )

    return response.status_code


def print_list():

    # Build set of followers for the primary user
    followers = set()
    for data in git.get_user().get_followers().get_page(0):
        followers.add(data)

    print('List of non-followers\n=====================')
    for user in git.get_user().get_following().get_page(0):

        # If a user is in this following list but is not
        # following the primary user, then we can conclude
        # that this is not a mutual follow.

        # Print GitHub username and name (if set)
        if user not in followers:
            to_be_unfollowed.append(user.login)
            print(f'Username: {user.login}')
            if user.name is not None:
                print(f'Name: {user.name}')
            print()


print_list()

prompt = input('Unfollow all? [y] [n]')
while (
            prompt != "y" or
            prompt != "yes" or
            prompt != "n" or
            prompt != "no"
        ):
    if prompt == "y" or prompt == "yes":
        for user in to_be_unfollowed:
            unfollow_user(user)
    elif prompt == "n" or prompt == "no":
        break
    else:
        prompt = input("Try again:").lower()
