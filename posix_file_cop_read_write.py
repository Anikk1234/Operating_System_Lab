import argparse
import sys
import os

def parse_octal(value_str, field_name):

    if len(value_str) != 4:
        sys.stderr.write(f"Error: {field_name} must be exactly 4 digits (e.g., 0755).\n")
        sys.exit(1)

    if not value_str.startswith('0'):
        sys.stderr.write(f"Error: {field_name} must start with a leading zero.\n")
        sys.exit(1)

    for char in value_str:
        if char not in '01234567':
            sys.stderr.write(f"Error: {field_name} contains invalid octal digits.\n")
            sys.exit(1)

    try:
        return int(value_str, 8)
    except ValueError:
        sys.stderr.write(f"Error: Invalid octal format for {field_name}.\n")
        sys.exit(1)


def get_symbolic_string(mode):
    perms = "rwxrwxrwx"
    symbolic = ""
    mode = mode & 0o777

    for i in range(9):
        shift = 8 - i
        if mode & (1 << shift):
            symbolic += perms[i]
        else:
            symbolic += "-"
    return symbolic


def main():
    parser = argparse.ArgumentParser(description="UNIX Permission Calculator", add_help=False)

    # Define arguments manually to control error messages strictly
    parser.add_argument("--mode", type=str, required=True, help="Base mode (octal, 4 digits)")
    parser.add_argument("--umask", type=str, default="0000", help="Umask (octal, 4 digits)")

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)
    except SystemExit:

        sys.exit(1)

    mode_val = parse_octal(args.mode, "--mode")
    umask_val = parse_octal(args.umask, "--umask")

    effective_mode = (mode_val & (~umask_val)) & 0o777

    eff_octal_str = f"{effective_mode:04o}"

    eff_symbolic_str = get_symbolic_string(effective_mode)

    print(f"OK: EFFECTIVE {eff_octal_str}")
    print(f"OK: SYMBOLIC {eff_symbolic_str}")

if __name__ == "__main__":
    main()