import os
import sys
import stat

def main():
    if len(sys.argv) > 1:
        search_path = sys.argv[1]
    else:
        search_path = "."

    try:
        if not os.path.isdir(search_path):
            print(f"Error: '{search_path}' is not a directory.")
            sys.exit(1)

        print(f"Listing for: {os.path.abspath(search_path)}")
        print("-" * 65)
        # Header formatting
        print(f"{'Name':<25} | {'Inode':<10} | {'Size':<10} | {'Mode':<5}")
        print("-" * 65)

        for filename in os.listdir(search_path):
            full_path = os.path.join(search_path, filename)

            file_info = os.stat(full_path)

            inode = file_info.st_ino
            size = file_info.st_size

            mode_octal = stat.S_IMODE(file_info.st_mode)

            print(f"{filename:<25} | {inode:<10} | {size:<10} | {mode_octal:03o}")

    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()