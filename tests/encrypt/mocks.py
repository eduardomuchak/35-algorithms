from challenges.challenge_encrypt_message import encrypt_message


def encrypt_does_nothing(message: str, key: int):
    pass


def encrypt_reversed_mod(message: str, key: int):
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


def encrypt_any_range_for_key(message: str, key: int):
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


def encrypt_sorted_not_reversed(message: str, key: int):
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = sorted(message[:key])
    part_two = sorted(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


def encrypt_no_type_validation(message: str, key: int):

    if isinstance(message, str) and isinstance(key, int):
        return encrypt_message(message, key)

    return None
