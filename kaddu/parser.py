import re
from typing import List
from .models import Node


def clean_lines(content: str) -> List[str]:
    lines = content.splitlines()
    cleaned = []

    for line in lines:
        if line.strip().startswith("```"):
            continue
        if not line.strip():
            continue

        cleaned.append(line.rstrip())

    return cleaned


def get_depth_and_name(line: str):
    line = line.rstrip()

    if re.fullmatch(r"[\s│├└─]+", line):
        return None, None

    match = re.search(r"[├└]", line)

    if match:
        prefix_length = match.start()
        depth = prefix_length // 4 + 1
        name = re.sub(r"^[\s│├└─]+", "", line).strip()
    else:
        depth = 0
        name = line.strip()

    if not name:
        return None, None

    return depth, name


def parse_structure(content: str) -> Node:
    lines = clean_lines(content)

    stack = []
    root = None

    for raw_line in lines:

        result = get_depth_and_name(raw_line)
        if result == (None, None):
            continue
        depth, name = result

        is_file = not name.endswith("/")
        name = name.rstrip("/")

        node = Node(name=name, is_file=is_file)

        while stack and stack[-1][0] >= depth:
            stack.pop()

        if stack:
            parent_node = stack[-1][1]
            parent_node.add_child(node)
        else:
            root = node

        stack.append((depth, node))

    if root is None:
        raise ValueError("Invalid structure format")

    return root