from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class ThemeFile:
    """
    테마에 포함된 파일
    """

    name: str
    path: Path
    relative_path: str
    suffix: str
    size: int


@dataclass(slots=True)
class ThemeImage:
    """
    이미지 리소스
    """

    name: str
    path: Path
    relative_path: str

    width: int = 0
    height: int = 0

    exists: bool = True


@dataclass(slots=True)
class CssRule:
    """
    CSS Rule 하나
    """

    selector: str

    properties: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class ThemeModel:
    """
    프로젝트 전체에서 사용하는 Theme 객체
    """

    root: Path | None = None

    css_file: Path | None = None

    manifest_file: Path | None = None

    files: list[ThemeFile] = field(default_factory=list)

    images: list[ThemeImage] = field(default_factory=list)

    css_rules: list[CssRule] = field(default_factory=list)

    colors: dict[str, str] = field(default_factory=dict)

    metadata: dict[str, str] = field(default_factory=dict)

    variables: dict[str, str] = field(default_factory=dict)

    image_lookup: dict[str, ThemeImage] = field(default_factory=dict)

    def clear(self):

        self.files.clear()

        self.images.clear()

        self.css_rules.clear()

        self.colors.clear()

        self.metadata.clear()

        self.variables.clear()

        self.image_lookup.clear()

    def add_file(self, file: ThemeFile):

        self.files.append(file)

    def add_image(self, image: ThemeImage):

        self.images.append(image)

        self.image_lookup[image.name] = image

    def add_rule(self, rule: CssRule):

        self.css_rules.append(rule)

    def image(self, filename: str) -> ThemeImage | None:

        return self.image_lookup.get(filename)

    def property(self, selector: str, name: str):

        for rule in self.css_rules:

            if rule.selector == selector:

                if name in rule.properties:

                    return rule.properties[name]

        return None

    @property
    def image_count(self):

        return len(self.images)

    @property
    def css_count(self):

        return len(self.css_rules)

    @property
    def file_count(self):

        return len(self.files)
