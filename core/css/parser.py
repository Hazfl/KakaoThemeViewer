from __future__ import annotations

import re
from pathlib import Path

from .model import (
    CssColorValue,
    CssImageValue,
    CssRule,
    CssValue,
)


URL_PATTERN = re.compile(r"url\((.*?)\)", re.IGNORECASE)
RULE_PATTERN = re.compile(r"([^{]+)\{([^}]*)\}", re.DOTALL)


class CssParser:

    def parse_file(self, path: str | Path) -> list[CssRule]:

        path = Path(path)

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return self.parse(f.read())

    def parse(self, text: str) -> list[CssRule]:

        text = self._remove_comments(text)

        rules: list[CssRule] = []

        for selector, body in RULE_PATTERN.findall(text):

            selector = selector.strip()

            if not selector:
                continue

            rule = CssRule(selector)

            for line in body.split(";"):

                line = line.strip()

                if not line:
                    continue

                if ":" not in line:
                    continue

                name, value = line.split(":", 1)

                name = name.strip()
                value = value.strip()

                rule.add(
                    name,
                    self._parse_value(value),
                )

            rules.append(rule)

        return rules

    def _remove_comments(self, text: str) -> str:

        while "/*" in text:

            start = text.find("/*")

            end = text.find("*/", start)

            if end == -1:
                break

            text = text[:start] + text[end + 2 :]

        return text

    def _parse_value(self, value: str):

        lower = value.lower()

        url = URL_PATTERN.search(value)

        if url:

            filename = (
                url.group(1)
                .replace('"', "")
                .replace("'", "")
                .strip()
            )

            return CssImageValue(
                raw=value,
                filename=filename,
            )

        if lower.startswith("#"):

            return CssColorValue(
                raw=value,
                color=value,
            )

        if lower.startswith("rgb"):

            return CssColorValue(
                raw=value,
                color=value,
            )

        if lower.startswith("rgba"):

            return CssColorValue(
                raw=value,
                color=value,
            )

        return CssValue(value)
