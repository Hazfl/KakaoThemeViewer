from __future__ import annotations

from pathlib import PurePosixPath

from core.theme_model import ThemeModel
from .model import CssImageValue


class CssResolver:
    """
    CSS의 url(...)과 실제 ThemeImage를 연결한다.
    """

    def resolve(self, theme: ThemeModel) -> None:

        image_map = {}

        for image in theme.images:

            image_map[image.name.lower()] = image
            image_map[image.relative_path.lower()] = image

        for rule in theme.css_rules:

            for prop in rule.properties:

                value = prop.value

                if not isinstance(value, CssImageValue):
                    continue

                key = value.filename.replace("\\", "/").strip().lower()

                image = image_map.get(key)

                if image is None:
                    key = PurePosixPath(key).name.lower()
                    image = image_map.get(key)

                if image is None:
                    continue

                value.relative_path = image.relative_path
