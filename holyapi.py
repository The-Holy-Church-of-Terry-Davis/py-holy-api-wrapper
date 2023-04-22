import json
import requests


class helper:
    def getEndpoint(endpoint: str) -> tuple[int, str]:
        """Returns a tuple with the status code and the response.
        
        Args:
            endpoint (str): The endpoint. Ex. `/status`.

        Returns:
            `tuple[status_code: int, response: str]`
        
        """
        url = f"https://api.thcotd.repl.co{endpoint}"
        resp = requests.get(url)

        if resp.ok:
            return (200, resp.json())
        else:
            return (resp.status_code, resp.content())

# /status
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
    what = what.lower()
    if what not in ["status", "message", "all"]:
        raise KeyError(f'Unknown field: "{what}"  -  Fields known: "status", "message", "all"')

    response = helper.getEndpoint(endpoint="/status")
    if response[0] == 200:  # i did something - statment#0700 🤯🤑🤑
        if return_as_json or what == "all":
            return response[1]
        return response[1][what]  # real!

    return f"Something went wrong while requesting /status! HTTP code: {response[0]}"

# /info
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
    
    if what not in ["infoMessage", "discord", "gh_organization", "our_website", "repository", "all"]:
        raise KeyError(f'Unknown field: "{what}"  -  Fields known: "infoMessage", "discord", "gh_organization", "our_website", "repository", "all"')

    response = helper.getEndpoint(endpoint="/info")
    if response[0] == 200:
        if return_as_json or what == "all":
            return response[1]
        elif what in ["discord", "gh_organization", "our_website", "repository"]:
            return response[1]["links"][what]
        return response[1][what]

    return f"Something went wrong while requesting /info! HTTP code: {response[0]}"


# /vocab
def vocab() -> str:
    """Literally returns `vocab.txt`. Be careful, this is a very large file.
    """
    return helper.getEndpoint(endpoint="/vocab")

# /godsay?amount=1
def godsay(amount=1, return_as_json=False) -> str:
    """Returns random words from God.

    Args:
        amount (int): the amount of words you want.
        return_as_json (bool): whether to return the data as JSON or not.
    """
    response = helper.getEndpoint(endpoint=f"/godsay?amount={amount}")
    if response[0] == 200:
        if return_as_json:
            return response[1]

        return response[1]["godsay"]

    return f"Something went wrong while requesting /godsay! HTTP code: {response[0]}"


# /quote?amount=1
def quote(amount=1, return_as_json=False):
    """Returns quotes from Terry.

    Args:
        amount (int): the amount of words you want.
        return_as_json (bool): whether to return the data as JSON or not.
    """
    response = helper.getEndpoint(endpoint=f"/quote?amount={amount}")
    if response[0] == 200:
        if return_as_json:
            return response[1]

        quotes = ""
        for i in response[1]["quotes"]:
            add_quote = f"{i}.\n"
            if i[-1] == ".":
                add_quote = f"{i}\n"
                
            quotes += add_quote
        
        return quotes

    return f"Something went wrong while requesting /quote! HTTP code: {response[0]}"


# /divineintellect
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
    if what not in ["divineIntellect", "message", "all"]:
        raise KeyError(f'Unknown field: "{what}"  -  Fields known: "divineIntellect", "message", "all"')

    response = helper.getEndpoint(endpoint="/divineintellect")
    if response[0] == 200:
        if return_as_json or what == "all":
            return response[1]

        return response[1][what]

    return f"Something went wrong while requesting /divineintellect! HTTP code: {response[0]}"


# /askterry
def askterry(return_as_json=False) -> str:
    """Returns Terry's anwer.

    Args:
        return_as_json (bool): whether to return the data as JSON or not.
    """
    response = helper.getEndpoint(endpoint=f"/askterry")
    if response[0] == 200:
        if return_as_json:
            return response[1]

        return response[1]["answer"]

    return f"Something went wrong while requesting /askterry! HTTP code: {response[0]}"
