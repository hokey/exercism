SECRET_COMMANDS = {
    1: 'jump',
    2: 'close your eyes',
    3: 'double blink',
    4: 'wink'
}


def commands(binary_str):
    """
    Given a binary string, give the kids secret handshake commands

    :param str binary_str: Secret code in binary
    :return list[str]: list of commands to do
    """
    secrets = []
    reverse = False
    if binary_str[0] == '1':
        reverse = True
    for index in range(1,len(binary_str)):
        if binary_str[index] == '1':
            secrets.append(SECRET_COMMANDS[index])
    if not reverse:
        secrets = list(reversed(secrets))
    return secrets
        
