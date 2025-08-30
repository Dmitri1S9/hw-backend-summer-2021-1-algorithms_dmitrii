from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        res = []
        stack = [self._root]
        visited = set()
        while stack:
            node = stack.pop()
            if node not in visited:
                res.append(node)
                visited.add(node)
                stack.extend(reversed(node.outbound))
        return res

    def bfs(self) -> list[Node]:
        res = [self._root]
        root = self._root
        next_level = root.outbound
        while next_level:
            new_next_level = list()
            for node in next_level:
                if node not in res:
                    res.append(node)
                    for node_p in node.outbound:
                        if node_p not in next_level:
                            new_next_level.append(node_p)
            next_level = [i for i in new_next_level if i not in res]

        return res
