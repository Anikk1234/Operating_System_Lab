import sys


def solve(name, blocks, procs):
    holes = blocks[:]  # Copy
    print(f"ALG {name}")
    count = 0

    for i, p in enumerate(procs):
        idx = -1
        if name == "FIRST_FIT":
            for j, h in enumerate(holes):
                if h >= p: idx = j; break
        elif name == "BEST_FIT":
            best = float('inf')
            for j, h in enumerate(holes):
                if h >= p and (h - p) < best: best = h - p; idx = j
        elif name == "WORST_FIT":
            worst = -1
            for j, h in enumerate(holes):
                if h >= p and h > worst: worst = h; idx = j

        if idx != -1:
            print(f"PROC {i} SIZE {p} -> BLOCK {idx}")
            holes[idx] -= p
            count += 1
        else:
            print(f"PROC {i} SIZE {p} -> FAIL")
    print(f"OK: ALLOCATED {count}/{len(procs)}")


def main():
    lines = sys.stdin.read().strip().split('\n')
    B = list(map(int, lines[1].split()))
    P = list(map(int, lines[3].split()))
    solve("FIRST_FIT", B, P)
    solve("BEST_FIT", B, P)
    solve("WORST_FIT", B, P)


if __name__ == "__main__": main()

#printf "3\n10 20 5\n4\n6 8 21 5" | python3 memfit.py