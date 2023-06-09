# gitfluencer

This is a simple Python script designed to identify non-mutual followers
and allows for a quick, mass-unfollow solution, saving you the hassle
of manually identifying and unfollowing each account individually.

![image](https://user-images.githubusercontent.com/100006388/232710218-0fee7061-3291-4fbc-b453-e43776c2bab4.png)

## Features

* Fetches the list of GitHub accounts that you are following.
* Identifies the non-mutual followers who are not following you back.
* Provides the option to unfollow all the non-mutual followers in one go.

## Requirements

* Python 3.x
* GitHub account with valid credentials

## How to Use

1. Clone or download the script to your local machine

2. Install the required dependencies with 

    ```terminal
    pip install -r requirements.txt
    ```

3. Create a `.env` file according to the [.env.example](/.env.example)

4. Run the script with 

    ```terminal
    python3 src/main.py
    ```
