import sys


def main():
    lines = sys.stdin.read().strip().split('\n')
    procs = []
    for line in lines[1:]:
        if not line: continue
        p = line.split(',')
        procs.append({'pid': p[0], 'arr': int(p[1]), 'bst': int(p[2]), 'prio': int(p[3])})

    n = len(procs)
    completed = []
    time, total_wait, total_tat = 0, 0, 0
    gantt = []

    while len(completed) < n:
        avail = [p for p in procs if p['arr'] <= time and p not in completed]

        if not avail:
            uncomp = [p for p in procs if p not in completed]
            time = min(p['arr'] for p in uncomp)
            continue

        # Aging: Effective Prio = Base - WaitingTime
        best_p = min(avail, key=lambda p: (p['prio'] - (time - p['arr']), p['arr'], p['pid']))

        start = time
        time += best_p['bst']
        gantt.append(f"{best_p['pid']}@{start}-{time}")

        tat = time - best_p['arr']
        total_tat += tat
        total_wait += (tat - best_p['bst'])
        completed.append(best_p)

    print("ALG PRIO_AGING")
    print("GANTT " + " ".join(gantt))
    print(f"OK: AVG_WAIT {total_wait / n:.2f} AVG_TAT {total_tat / n:.2f}")


if __name__ == "__main__": main()



#printf "pid,arrival,burst,priority\nA,0,4,5\nB,1,2,0" | python3 schedprio.py