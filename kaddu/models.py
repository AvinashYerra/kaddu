from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    name: str
    is_file: bool
    children: List["Node"] = field(default_factory=list)

    def add_child(self, child: "Node") -> None:
        self.children.append(child)