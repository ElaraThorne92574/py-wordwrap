"""Greedy word wrap to a width. Standard library only."""


def wrap(text, width=80):
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line); line = word
        else:
            line = word if not line else line + " " + word
    if line:
        lines.append(line)
    return lines
