"""Structural router scaffold. No production claims at L0."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Router:
    name: str = "x4-router"
    version: str = "0.0.1"
    routes: dict[str, str] = field(default_factory=dict)

    def add_route(self, path: str, target: str) -> None:
        if not path or not target:
            raise ValueError("path and target are required")
        self.routes[path] = target

    def resolve(self, path: str) -> str | None:
        return self.routes.get(path)

    def health(self) -> dict[str, str]:
        return {"status": "ok", "server": self.name, "version": self.version}
