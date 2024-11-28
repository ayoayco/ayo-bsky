# ayo-bsky

just wanna automate some bsky posts...

## Why

Because why not

## Development

1. Set up your **Debian** (for other environments, search for counterpart instructions)

    ```bash
    # update repositories
    $ sudo apt update

    # install python stuff
    $ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv
    ```

2. Install dependencies

    ```bash
    # clone the project 
    $ git clone git@github.com:ayoayco/ayo-bsky

    # go into the project directory
    $ cd ayo-bsky

    # create config file from example
    $ cp example_config.txt config.txt

    # add your bsky app password in the config.txt file

    # create python environment:
    $ python3 -m venv .venv

    # activate python env:
    $ . .venv/bin/activate

    # install deps:
    (.venv)$ python -m pip install -r requirements.txt

    # rejoice!
    ```

3. To run the script:
    ```bash
    (.venv)$ python app.py
    ```

