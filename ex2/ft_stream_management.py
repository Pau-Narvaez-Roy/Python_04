#!/usr/bin/env python3
import sys


def ft_read_file(name: str) -> str:
    fd = open(name, "r")
    print("---\n")
    txt: str = fd.read()
    print(txt)
    print("\n---")
    fd.close()
    print(f"File '{name}' closed.\n")
    return txt


def ft_transform(txt: str) -> None:
    print("---\n")
    lst = txt.split('\n')
    for i in range(len(lst)):
        lst[i] += '#'
    saved = "\n".join(lst)
    print(saved)
    print("\n---")
    print("Enter new file name (or empty):", end=' ')
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip("\n")
    if new_file:
        print(f"Saving data to '{new_file}'")
        fd = open(new_file, "w")
        fd.write(saved)
        print(f"Data saved in file '{new_file}'")
        fd.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            txt = ft_read_file(sys.argv[1])
            print("Transform data:")
            ft_transform(txt)
        except Exception as e:
            file = sys.stderr
            file.write(f" [STDERR] Error opening file '{sys.argv[1]}': {e}")
    else:
        print("Usage: ft_stream_management.py <file>\n")
