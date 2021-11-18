FILE_NAME = "school-work.txt"

DEFAULT_TEXT = "Could not find article."


def write(text: str) -> bool:
    with open(FILE_NAME, "w") as file:
        file.write(text)
    return True
