from dataclasses import dataclass, field


@dataclass
class Path:
    x: int
    y: int
    neighbors: list['Path'] = field(default_factory=list)
    traced: bool = False
