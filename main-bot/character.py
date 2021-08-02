from typing import List

class Character:
    def __init__(self, name: str, default_name: str, version: int, respectthreads: List[int]):
        self.name = name
        self.default_name = default_name
        self.version = version
        self.respectthreads = respectthreads