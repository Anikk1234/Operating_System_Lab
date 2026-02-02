import sys, argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--max', type=int)
    parser.add_argument('--start', type=int)
    parser.add_argument('--dir')
    args, _ = parser.parse_known_args()

    reqs = list(map(int, sys.stdin.read().split()[1:]))

    # SCAN Logic
    print("ALG SCAN")
    left = sorted([r for r in reqs if r < args.start])
    right = sorted([r for r in reqs if r >= args.start])

    if args.dir == "right":
        path = right + [args.max] + left[::-1]
    else:
        path = left[::-1] + [0] + right

    # Filter out boundaries if not in requests, but keep order
    # (Usually we report service order, so remove max/0 if not requested)
    seq = [p for p in path if p in reqs]

    # Calculate moves: Start -> Path[0] -> Path[1]...
    moves = 0
    curr = args.start
    # Full path includes the bounce at boundary
    full_path = right + [args.max] + left[::-1] if args.dir == "right" else left[::-1] + [0] + right

    for p in full_path:
        moves += abs(p - curr)
        curr = p

    print("OK: ORDER " + " ".join(map(str, seq)))
    print(f"OK: MOVES {moves}")


if __name__ == "__main__": main()


#printf "5\n55 58 39 18 90" | python3 disksched.py --max 199 --start 50 --dir right