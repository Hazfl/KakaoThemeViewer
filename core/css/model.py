from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class CssValue:
    raw: str


@dataclass(slots=True)
class CssImageValue(CssValue):
    filename: str = ""
    relative_path: str | None = None
    resolved: bool = False


@dataclass(slots=True)
class CssColorValue(CssValue):
    color: str = ""


@dataclass(slots=True)
class CssProperty:
    name: str
    value: CssValue


@dataclass(slots=True)
class CssRule:
    selector: str

    properties: list[CssProperty] = field(default_factory=list)

    def add(
        self,
        name: str,
        value: CssValue,
    ):

        self.properties.append(
            CssProperty(
                name=name,
                value=value,
            )
        )

    def get(self, name: str):

        for prop in self.properties:

            if prop.name == name:
                return prop.value

        return None
