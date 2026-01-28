import sys, argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--pattern');
    parser.add_argument('--files')
    args = parser.parse_args()

    if not args.pattern: print("ERROR: E_EMPTY"); sys.exit(1)

    matches, count = 0, 0
    for fname in args.files.split(','):
        if not fname: continue
        count += 1
        try:
            with open(fname, 'r') as f:
                for i, line in enumerate(f, 1):
                    if args.pattern in line:
                        print(f"MATCH {fname}:{i}:{line.rstrip()}")
                        matches += 1
        except:
            print(f"ERROR: E_OPEN {fname}"); sys.exit(1)
    print(f"OK: MATCHES {matches} FILES {count}")


if __name__ == "__main__": main()


# # Create dummy files
# echo "TODO: Fix bug" > a.c
# echo "int main() {}" > b.c
# # Run grep
# python3 greplite.py --pattern TODO --files a.c,b.c