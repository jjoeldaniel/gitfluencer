from github import Github
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
import os
import requests


def unfollow_user(target_username: str, api_token: str):
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


def print_list(git: Github, to_be_unfollowed: list):

    # Table to be printed
    table = Table(title='List of non-followers')
    table.add_column('GitHub Username', style='green')
    table.add_column('Name (if available)', justify='right', style='cyan')

    # Build set of followers for the primary user
    followers = set()

    x = 0
    while len(git.get_user().get_followers().get_page(x)) > 0:
        for data in git.get_user().get_followers().get_page(x):
            followers.add(data)
        x += 1

    y = 0
    while len(git.get_user().get_followers().get_page(y)) > 0:
        for user in git.get_user().get_following().get_page(y):

            # If a user is in this following list but is not
            # following the primary user, then we can conclude
            # that this is not a mutual follow.

            # Print GitHub username and name (if set)
            if user not in followers:
                to_be_unfollowed.append(user.login)
                if user.name is not None:
                    table.add_row(user.login, user.name)
                else:
                    table.add_row(user.login)

        y += 1

    console = Console()
    console.print(table)


def main():

    # Get API token from environment variable or prompt for input
    api_token = os.getenv("GH_API_TOKEN")
    if not api_token:
        api_token = Prompt.ask(
                "Please enter your GitHub API token: ",
                password=True,
                show_default=False,
                show_choices=True)

    # Store API token as environment variable
    os.environ["GH_API_TOKEN"] = api_token

    # Create API object from token
    git = Github(api_token)
    to_be_unfollowed = list()

    print_list(git, to_be_unfollowed)

    # Confirmation
    prompt = Prompt.ask('Unfollow all? [y] [n]', choices=['y', 'n'])
    if prompt == "y" or prompt == "yes":
        confirm = Confirm.ask("Are you sure?")
        if confirm:
            for user in to_be_unfollowed:
                unfollow_user(target_username=user, api_token=api_token)
    elif prompt == "n" or prompt == "no":
        print('Goodbye!')


if __name__ == "__main__":
    main()
