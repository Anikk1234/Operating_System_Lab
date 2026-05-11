import sys, argparse


def calculate_moves(start, full_path):
    """Helper function to calculate total head movements given a path."""
    moves = 0
    curr = start
    for p in full_path:
        moves += abs(p - curr)
        curr = p
    return moves


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--max', type=int)
    parser.add_argument('--start', type=int)
    parser.add_argument('--dir')
    args, _ = parser.parse_known_args()

    # Read requests, ignoring the first number (the count)
    reqs = list(map(int, sys.stdin.read().split()[1:]))

    # ==========================================
    # 1. FCFS (First-Come, First-Served)
    # ==========================================
    print("ALG FCFS")
    fcfs_moves = calculate_moves(args.start, reqs)
    print("OK: ORDER " + " ".join(map(str, reqs)))
    print(f"OK: MOVES {fcfs_moves}")

    # ==========================================
    # 2. SSTF (Shortest Seek Time First)
    # ==========================================
    print("ALG SSTF")
    unvisited = reqs[:]
    curr = args.start
    sstf_order = []
    sstf_moves = 0

    while unvisited:
        # Find the closest request. 
        # Tie breaker: x ensures if distances are equal, the smaller cylinder is picked.
        closest = min(unvisited, key=lambda x: (abs(x - curr), x))
        sstf_moves += abs(closest - curr)
        curr = closest
        sstf_order.append(closest)
        unvisited.remove(closest)

    print("OK: ORDER " + " ".join(map(str, sstf_order)))
    print(f"OK: MOVES {sstf_moves}")

    # --- Common Setup for SCAN and C-SCAN ---
    left = sorted([r for r in reqs if r < args.start])
    right = sorted([r for r in reqs if r >= args.start])

    # ==========================================
    # 3. SCAN
    # ==========================================
    print("ALG SCAN")
    if args.dir == "right":
        scan_order = right + left[::-1]
        scan_full_path = right + [args.max] + left[::-1]
    else:
        scan_order = left[::-1] + right
        scan_full_path = left[::-1] + [0] + right

    scan_moves = calculate_moves(args.start, scan_full_path)
    print("OK: ORDER " + " ".join(map(str, scan_order)))
    print(f"OK: MOVES {scan_moves}")

    # ==========================================
    # 4. C-SCAN (Circular SCAN)
    # ==========================================
    print("ALG C-SCAN")
    if args.dir == "right":
        cscan_order = right + left
        # Goes to max, jumps to 0, then goes to highest request on the left
        cscan_full_path = right + [args.max, 0] + left
    else:
        cscan_order = left[::-1] + right[::-1]
        # Goes to 0, jumps to max, then goes to lowest request on the right
        cscan_full_path = left[::-1] + [0, args.max] + right[::-1]

    cscan_moves = calculate_moves(args.start, cscan_full_path)
    print("OK: ORDER " + " ".join(map(str, cscan_order)))
    print(f"OK: MOVES {cscan_moves}")


if __name__ == "__main__": main()