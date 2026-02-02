import sys, argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--pagesize', type=int, default=256)
    parser.add_argument('--tlb', type=int, default=0)
    args, _ = parser.parse_known_args()

    data = iter(sys.stdin.read().split())
    N = int(next(data))
    pt = {}
    for _ in range(N):
        v, p, valid = int(next(data)), int(next(data)), int(next(data))
        if valid: pt[v] = p

    tlb_c, hits, miss = {}, 0, 0
    Q = int(next(data))

    for _ in range(Q):
        va = int(next(data))
        vpn, off = va // args.pagesize, va % args.pagesize
        pa, status = -1, ""

        if args.tlb > 0:
            if vpn in tlb_c:
                pa = tlb_c[vpn] * args.pagesize + off
                status = "(TLB HIT)";
                hits += 1
            else:
                status = "(TLB MISS)";
                miss += 1
                if vpn in pt:
                    pa = pt[vpn] * args.pagesize + off
                    tlb_c[vpn] = pt[vpn]  # Simple update
                else:
                    print(f"OK: VA {va} -> PAGEFAULT");
                    continue
            print(f"OK: VA {va} -> PA {pa} {status}")
        else:
            if vpn in pt:
                print(f"OK: VA {va} -> PA {pt[vpn] * args.pagesize + off}")
            else:
                print(f"OK: VA {va} -> PAGEFAULT")

    if args.tlb > 0: print(f"OK: TLB_HITS {hits} TLB_MISSES {miss}")


if __name__ == "__main__": main()

#printf "1 0 1 1 2 10 10" | python3 pagetrans.py --tlb 4