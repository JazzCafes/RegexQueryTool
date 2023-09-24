import argparse
import re
import os

def main():
    """Searches for matches of a regular expression pattern in a file."""
    parser = argparse.ArgumentParser(description="Regex Query Tool")
    parser.add_argument("pattern", help="Regular expression pattern")
    parser.add_argument("file", help="File name")

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' does not exist.")
        return

    try:
        re.compile(args.pattern)
    except re.error:
        print(f"Error: Invalid regular expression pattern '{args.pattern}'.")
        return

    with open(args.file) as f:
        text = f.read()

    matches = re.findall(args.pattern, text)

    for match in matches:
        print(match)

if __name__ == "__main__":
    main()
