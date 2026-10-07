#!/usr/bin/env python3


def secure_archive(name: str, action: str, text: str) -> tuple[bool, str]:
    worked = False
    message = ""
    try:
        with open(name, action) as fd:
            if action == 'r':
                message = fd.read()
            elif action == 'w':
                fd.write(text)
                message = "Content successfully written to file"
            worked = True
    except Exception as e:
        message = str(e)
    return (worked, message)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistant file:")
    print(secure_archive("/not/existing/file", "r", ""), "\n")
    print("Using 'secure_archive' to read from a inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r", ""), "\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_text.txt", "r", ""), "\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new", "w", "HAIIIIII"))
