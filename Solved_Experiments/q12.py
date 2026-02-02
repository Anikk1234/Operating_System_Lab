import sys, argparse
from collections import deque


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--q', type=int, default=2)
    args, _ = parser.parse_known_args()

    lines = sys.stdin.read().strip().split('\n')
    procs = []
    for line in lines[1:]:
        if not line: continue
        p = line.split(',')
        procs.append({'pid': p[0], 'arr': int(p[1]), 'bst': int(p[2]), 'rem': int(p[2])})

    procs.sort(key=lambda x: (x['arr'], x['pid']))

    time, q = 0, deque()
    gantt, completed = [], []
    idx, n = 0, len(procs)

    # Add first processes
    while idx < n and procs[idx]['arr'] <= time:
        q.append(procs[idx]);
        idx += 1

    while q or idx < n:
        if not q:
            time = procs[idx]['arr']
            while idx < n and procs[idx]['arr'] <= time:
                q.append(procs[idx]);
                idx += 1

        p = q.popleft()
        run = min(args.q, p['rem'])
        start = time
        time += run
        p['rem'] -= run
        gantt.append(f"{p['pid']}@{start}-{time}")

        # Check arrivals during run
        while idx < n and procs[idx]['arr'] <= time:
            q.append(procs[idx]);
            idx += 1

        if p['rem'] > 0:
            q.append(p)
        else:
            p['fin'] = time
            completed.append(p)

    wt = sum(p['fin'] - p['arr'] - p['bst'] for p in completed)
    tat = sum(p['fin'] - p['arr'] for p in completed)

    print("ALG RR")
    print("GANTT " + " ".join(gantt))
    print(f"OK: AVG_WAIT {wt / n:.2f} AVG_TAT {tat / n:.2f}")


if __name__ == "__main__": main()


#printf "pid,arrival,burst\nP1,0,5\nP2,2,2\n" | python3 schedsim2.py --q 2