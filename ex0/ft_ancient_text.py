#!/usr/bin/env python3
import sys


def ft_read_file(name: str) -> None:
    try:
        fd = open(name, "r")
        print("---\n")
        print(fd.read())
        print("\n---")
        fd.close()
        print(f"File '{name}' closed.")
    except Exception as e:
        print(f"Error opening file '{name}': {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        ft_read_file(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>\n")
