BOBS_RESPONSES = {
    "SURE": "Sure.",
    "WHOA": "Whoa, chill out!",
    "CALM": "Calm down, I know what I'm doing!",
    "FINE": "Fine. Be that way!",
    "WHAT": "Whatever."
}

def is_shouting_unicode(checkstring) -> bool:
    """
    Return True if checkstring contains at least one uppercase letter (unicode) and no lowercase letters.
    
    :param str checkstring: the string to check for shouting
    :return bool: is the string shouting
    """
    has_upper = False
    for ch in checkstring:
        if ch.isalpha():
            if ch.islower():      # any lowercase letter -> not shouting
                return False
            if ch.isupper():
                has_upper = True
    return has_upper


def response(hey_bob):
    """
    Predict bob's responses based of the following criteria:

    - "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    - "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    - "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    - "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    - "Whatever." This is what he answers to anything else.
    
    :param str hey_bob: The statement sent to bob
    :return str: Bob's response based on his typical responses
    """
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?'):
        if is_shouting_unicode(hey_bob):
            return BOBS_RESPONSES["CALM"]
        else:
            return BOBS_RESPONSES["SURE"]
    elif is_shouting_unicode(hey_bob):
        return BOBS_RESPONSES["WHOA"]
    elif not hey_bob:
        return BOBS_RESPONSES["FINE"]
    else:
        return BOBS_RESPONSES["WHAT"]