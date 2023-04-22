# py-holy-api-wrapper

This is a Python wrapper for the Holy API. The Holy API provides access to divine messages and knowledge from Terry, as well as random quotes, information about the Holy Church of Terry Davis, and more.

API: https://api.thcotd.repl.co

## Requirements

- Requests, but literally everyone has it.
```sh
$ pip3 install requests
# or
$ python -m pip install requests
```

## Installation

As of now, this isn't on pypi. I'll add it soon and update the README when it's available.

1. Clone the repository with the following command:
```sh
$ git clone https://github.com/the-holy-church-of-terry-davis/py-holy-api-wrapper.git
```

2. Include the `holyapi.py` file in your project.
```py
import holyapi
```

## Usage

Here is an example:

```py
import holyapi

def main():
    print(f"""
Status       : {holyapi.status("status")}
Status Msg   : {holyapi.status("message")}

Info Message : {holyapi.info("infoMessage")}
Info Discord : {holyapi.info("discord")}
Info gh_org  : {holyapi.info("gh_organization")}
Info website : {holyapi.info("our_website")}
Info repo    : {holyapi.info("repository")}

Godsay (5)   : {holyapi.godsay(5)}

Quote (2)    :
{holyapi.quote(2)}

Divine Intel : {holyapi.divineintellect()}
Divine Msg   : {holyapi.divineintellect("message")}

Ask Terry    : {holyapi.askterry()}
""")

if __name__ == '__main__':
    main()
```

Arguments or something:

```py

def status(what="all", return_as_json=False):
    """Returns data from the `/status` endpoint.

    Args:
        what (str): What you want, reffered to as "field".
        return_as_json (bool): Whether or not you want it to return as JSON.
    
    Fields:
        `status`\n
        `message`\n
        `all`\n

    Returns:
        `str`
    """

def info(what="all", return_as_json=False) -> str:
    """Returns data from the `/info` endpoint.

    Args:
        what (str): What you want, reffered to as "field".
        return_as_json (bool): Whether or not you want it to return as JSON.
    
    Fields:
        `infoMessage`\n
        `discord`\n
        `gh_organization`\n
        `our_website`\n
        `repository`\n
        `all`\n

    Returns:
        `str`
    """

def vocab() -> str:
    """Literally returns `vocab.txt`. Be careful, this is a very large file.
    """

def godsay(amount=1, return_as_json=False) -> str:
    """Returns random words from God.

    Args:
        amount (int): the amount of words you want.
        return_as_json (bool): whether to return the data as JSON or not.
    """

def quote(amount=1, return_as_json=False):
    """Returns quotes from Terry.

    Args:
        amount (int): the amount of words you want.
        return_as_json (bool): whether to return the data as JSON or not.
    """

def divineintellect(what="divineIntellect", return_as_json=False) -> str:
    """Returns data from the `/divingintellect` endpoint.

    Args:
        what (str): What you want, reffered to as "field".
        return_as_json (bool): Whether or not you want it to return as JSON.
    
    Fields:
        `divineIntellect`\n
        `message`\n
        `all`\n

    Returns:
        `str`
    """

def askterry(return_as_json=False) -> str:
    """Returns Terry's anwer.

    Args:
        return_as_json (bool): whether to return the data as JSON or not.
    """



```

## Licensing

This wrapper is under the MIT License. See [LICENSE](./LICENSE) for more.