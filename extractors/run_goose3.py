#!/usr/bin/env python3
import gzip
from pathlib import Path

from goose3 import Goose
from output_util import python_dist_version, timer, write_output_json


def main():
    output = {}
    for path in Path("html").glob("*.html.gz"):
        with gzip.open(path, "rt", encoding="utf8") as f:
            html = f.read()
        item_id = path.stem.split(".")[0]
        g = Goose()
        article = g.extract(raw_html=html)
        output[item_id] = {"articleBody": article.cleaned_text}
    write_output_json(
        Path("output") / "goose3.json",
        output=output,
        version=python_dist_version("goose3"),
    )


if __name__ == "__main__":
    with timer("goose3", "Python"):
        main()
