import sys, argparse


def fmt(mem, f):
    res = mem[:] + [-1] * (f - len(mem))
    return " ".join(map(str, res))


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--frames', type=int)
    args, _ = parser.parse_known_args()

    refs = list(map(int, sys.stdin.read().split()[1:]))
    F = args.frames

    # FIFO
    mem, faults = [], 0
    for p in refs:
        if p not in mem:
            faults += 1
            if len(mem) < F:
                mem.append(p)
            else:
                mem.pop(0); mem.append(p)
    print(f"ALG FIFO\nOK: FAULTS {faults}\nOK: FINAL {fmt(mem, F)}")

    # LRU
    mem, faults = [], 0
    for p in refs:
        if p not in mem:
            faults += 1
            if len(mem) < F:
                mem.append(p)
            else:
                mem.pop(0); mem.append(p)
        else:
            mem.remove(p);
            mem.append(p)
    print(f"ALG LRU\nOK: FAULTS {faults}\nOK: FINAL {fmt(mem, F)}")

    # OPT
    mem, faults = [], 0
    for i, p in enumerate(refs):
        if p not in mem:
            faults += 1
            if len(mem) < F:
                mem.append(p)
            else:
                # Find farthest
                victim, farthest = -1, -1
                for mp in mem:
                    try:
                        idx = refs[i + 1:].index(mp)
                    except:
                        idx = float('inf')
                    if idx > farthest: farthest = idx; victim = mp
                mem.remove(victim);
                mem.append(p)
    print(f"ALG OPT\nOK: FAULTS {faults}\nOK: FINAL {fmt(mem, F)}")


if __name__ == "__main__": main()



#printf "12 1 2 3 2 4 1 2 5 2 1 2 3" | python3 pagerepl.py --frames 3