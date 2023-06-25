from typing import TextIO


def text_file_peek(file: TextIO, n: int) -> str:
    previousPosition = file.tell()
    content = file.read(n)
    # return to the previousPosition
    file.seek(previousPosition)
    return content


def text_file_peek_line(file: TextIO, number_of_lines=1) -> str:
    previousPosition = file.tell()
    content = ''
    for i in range(number_of_lines):
        content += str(file.readline())
    # return to the previousPosition
    file.seek(previousPosition)
    return content
