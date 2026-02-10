import re

BOBS_RESPONSES = {
    "SURE": "Sure.",
    "WHOA": "Whoa, chill out!",
    "CALM": "Calm down, I know what I'm doing!",
    "FINE": "Fine. Be that way!",
    "WHAT": "Whatever."
}

PATTERN = re.compile(
    r'^(?=.*[A-Z])[A-Z0-9\s!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]+$'
)

def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?'):
        if PATTERN.fullmatch(hey_bob):
            return BOBS_RESPONSES["CALM"]
        else:
            return BOBS_RESPONSES["SURE"]
    elif PATTERN.fullmatch(hey_bob):
        return BOBS_RESPONSES["WHOA"]
    elif not hey_bob:
        return BOBS_RESPONSES["FINE"]
    else:
        return BOBS_RESPONSES["WHAT"]