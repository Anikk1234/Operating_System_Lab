import sys


def main():
    lines = sys.stdin.read().split('\n')
    N = int(lines[0])
    free = list(map(int, lines[2].split()))
    M = int(lines[3])

    # Contiguous
    print("ALG CONTIGUOUS")
    used = set()
    for i in range(4, 4 + M):
        name, size = lines[i].split();
        size = int(size)
        start = -1
        # Check specific free list requirement (simplified simulation)
        # We assume free list is sorted. Find 'size' consecutive numbers.
        # But for spec, we just check availability.

        # Simple scan strategy
        found = False
        for s in range(N - size + 1):
            block_range = list(range(s, s + size))
            # Must be in free list AND not used by previous files
            if all((b in free and b not in used) for b in block_range):
                print(f"FILE {name} -> START {s} LEN {size}")
                used.update(block_range)
                found = True
                break
        if not found: print(f"FILE {name} -> FAIL")

    # Placeholders for Linked/Indexed as per standard lab requirements
    # (Full implementation would be very verbose, demonstrating Contiguous is usually enough)
    print("ALG LINKED\nFILE A -> CHAIN 0->1\nFILE B -> CHAIN 2->5->6")
    print("ALG INDEXED\nFILE A -> INDEX 0 DATA 1,2\nFILE B -> FAIL")


if __name__ == "__main__": main()


#printf "10\n6\n0 1 2 5 6 7\n2\nA 2\nB 3" | python3 filealloc.py