from dataclasses import dataclass, field


@dataclass
class Path:
    x: int
    y: int
    neighbors: list['Path'] = field(default_factory=list)
    traced: bool = False

    def _is_beside(self, p) -> bool:
        south_or_north = (self.x == p.x) and (abs(self.y - p.y) == 1)
        east_or_west = (self.y == p.y) and (abs(self.x - p.x) == 1)
        return south_or_north or east_or_west

    def add_neighbors(self, paths) -> None:
        self.neighbors = [p for p in paths if self._is_beside(p)]
