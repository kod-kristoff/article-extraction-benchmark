#!/usr/bin/env python3
import gzip
from pathlib import Path

import trafilatura
from output_util import python_dist_version, timer, write_output_json


def main():
    output = {}
    for path in Path("html").glob("*.html.gz"):
        with gzip.open(path, "rt", encoding="utf8") as f:
            html = f.read()
        item_id = path.stem.split(".")[0]
        output[item_id] = {
            "articleBody": trafilatura.extract(html, include_comments=False)
        }
    write_output_json(
        Path("output") / "trafilatura.json",
        output=output,
        version=python_dist_version("trafilatura"),
    )


if __name__ == "__main__":
    with timer("trafilatura", "Python"):
        main()
