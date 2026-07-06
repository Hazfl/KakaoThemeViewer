from __future__ import annotations

from pathlib import Path

from core.theme_model import (
    ThemeFile,
    ThemeImage,
    ThemeModel,
)
from core.css import CssParser

IMAGE_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".bmp",
}


CSS_SUFFIXES = {
    ".css",
}


MANIFEST_NAMES = {
    "manifest.xml",
    "theme.xml",
}


class ThemeLoader:

    def load(self, folder: str | Path) -> ThemeModel:

        root = Path(folder)

        if not root.exists():
            raise FileNotFoundError(root)

        model = ThemeModel()
        model.root = root

        self._scan(root, model)
        
        if model.css_file:
        
            parser = CssParser()
        
            model.css_rules.extend(
                parser.parse_file(model.css_file)
            )
        
        return model

    def _scan(
        self,
        root: Path,
        model: ThemeModel,
    ):

        for path in sorted(root.rglob("*")):

            if not path.is_file():
                continue

            relative = path.relative_to(root)

            file = ThemeFile(
                name=path.name,
                path=path,
                relative_path=str(relative).replace("\\", "/"),
                suffix=path.suffix.lower(),
                size=path.stat().st_size,
            )

            model.add_file(file)

            suffix = path.suffix.lower()

            if suffix in IMAGE_SUFFIXES:

                image = ThemeImage(
                    name=path.name,
                    path=path,
                    relative_path=file.relative_path,
                )

                model.add_image(image)

            if suffix in CSS_SUFFIXES:

                if model.css_file is None:
                    model.css_file = path

            if path.name.lower() in MANIFEST_NAMES:

                if model.manifest_file is None:
                    model.manifest_file = path
