import io
import pathlib
import sys

import yaml


def has_yaml_frontmatter(path):
    with open(path) as f:
        if f.readline().strip() != "---":
            return False
        return True


def parse_yaml_frontmatter(path):
    buffer = io.StringIO()
    with open(path) as f:
        f.readline()  # skip frontmatter header of "---"
        for line in f:
            if line.strip() == "---":
                break
            buffer.write(line)

    buffer.seek(0)
    return yaml.safe_load(buffer)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("source_path", type=pathlib.Path, default=pathlib.Path.cwd())
    parser.add_argument("--suffix", default=".md")

    args = parser.parse_args()
    if not args.suffix.startswith("."):
        args.suffix = "." + args.suffix
    glob_pat = f"*{args.suffix}"

    markdown_notebook_paths = []
    for path in args.source_path.rglob(glob_pat):
        if ".ipynb_checkpoints" in path.parts:
            continue
        if has_yaml_frontmatter(path):
            header = parse_yaml_frontmatter(path)
            if "kernelspec" in header:
                markdown_notebook_paths.append(path.as_posix())

    sys.stdout.write(" ".join(markdown_notebook_paths))
    sys.stdout.write("\n")
