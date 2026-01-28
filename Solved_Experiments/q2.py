import sys, os, zlib, argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--src');
    parser.add_argument('--dst');
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    if not args.src or not args.dst:
        print("ERROR: E_USAGE: missing args");
        sys.exit(1)

    if os.path.exists(args.dst) and not args.force:
        print("ERROR: E_EXISTS: destination already exists (use --force)");
        sys.exit(1)

    try:
        f_in = sys.stdin.buffer if args.src == '-' else open(args.src, 'rb')
        f_out = open(args.dst, 'wb')
        total, crc = 0, 0

        while chunk := f_in.read(4096):
            f_out.write(chunk)
            total += len(chunk)
            crc = zlib.crc32(chunk, crc)

        if args.src != '-': f_in.close()
        f_out.close()
        print(f"OK: COPIED {total} BYTES\nOK: CRC32 {crc & 0xFFFFFFFF:08x}")
    except Exception as e:
        print(f"ERROR: E_IO: {e}");
        sys.exit(1)


if __name__ == "__main__": main()

# # Create a test file
# echo "Hello OS Lab" > source.txt
# # Run the copy tool
# python3 fdcopy.py --src source.txt --dst dest.txt