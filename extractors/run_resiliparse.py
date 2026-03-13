#!/usr/bin/env python3
import gzip
from pathlib import Path

from output_util import python_dist_version, timer, write_output_json
from resiliparse.extract.html2text import extract_plain_text


def main():
    output = {}
    for path in Path("html").glob("*.html.gz"):
        with gzip.open(path, "rt", encoding="utf8") as f:
            html = f.read()
        item_id = path.stem.split(".")[0]
        output[item_id] = {"articleBody": extract_plain_text(html, main_content=True)}
    write_output_json(
        Path("output") / "resiliparse.json",
        output=output,
        version=python_dist_version("resiliparse"),
    )


if __name__ == "__main__":
    with timer("resiliparse", "Python"):
        main()
