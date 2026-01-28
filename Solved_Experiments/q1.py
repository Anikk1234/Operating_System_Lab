import sys
import argparse


def octal_to_symbolic(mode_int):
    mapping = {
        0: '---', 1: '--x', 2: '-w-', 3: '-wx',
        4: 'r--', 5: 'r-x', 6: 'rw-', 7: 'rwx'
    }
    user = (mode_int >> 6) & 7
    group = (mode_int >> 3) & 7
    other = mode_int & 7
    return mapping[user] + mapping[group] + mapping[other]


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--mode')
    parser.add_argument('--umask')
    args = parser.parse_args()

    if not args.mode:
        print("ERROR: E_USAGE: missing --mode")
        sys.exit(1)

    if len(args.mode) != 4 or not args.mode.isdigit():
        print("ERROR: E_OCTAL: mode must be 4-digit octal (0000-0777)")
        sys.exit(1)

    try:
        mode_val = int(args.mode, 8)
        if mode_val < 0 or mode_val > 0o777:
            raise ValueError
    except ValueError:
        print("ERROR: E_OCTAL: bad octal")
        sys.exit(1)

    umask_val = 0
    if args.umask:
        try:
            umask_val = int(args.umask, 8)
        except ValueError:
            print("ERROR: E_OCTAL: bad umask")
            sys.exit(1)

    effective = mode_val & (~umask_val) & 0o777

    print(f"OK: EFFECTIVE {effective:04o}")
    print(f"OK: SYMBOLIC {octal_to_symbolic(effective)}")


if __name__ == "__main__":
    main()



#python3 permcalc.py --mode 0644 --umask 0022