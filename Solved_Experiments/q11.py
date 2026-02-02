import sys


def solve_fcfs(procs):
    # Sort strictly by arrival time
    procs.sort(key=lambda x: (x['arr'], x['pid']))
    time, total_wait, total_tat = 0, 0, 0
    gantt = []

    for p in procs:
        if time < p['arr']: time = p['arr']  # Idle jump
        start = time
        time += p['bst']
        gantt.append(f"{p['pid']}@{start}-{time}")

        tat = time - p['arr']
        total_tat += tat
        total_wait += (tat - p['bst'])

    print("ALG FCFS")
    print("GANTT " + " ".join(gantt))
    print(f"OK: AVG_WAIT {total_wait / len(procs):.2f} AVG_TAT {total_tat / len(procs):.2f}")


def solve_sjf(procs):
    # Non-preemptive SJF
    n = len(procs)
    procs.sort(key=lambda x: (x['arr'], x['pid']))  # Initial sort
    completed = []
    time, total_wait, total_tat = 0, 0, 0
    gantt = []

    while len(completed) < n:
        # Find process that has arrived and is not done
        available = [p for p in procs if p['arr'] <= time and p not in completed]

        if not available:
            # Jump to next arrival
            uncompleted = [p for p in procs if p not in completed]
            time = min(p['arr'] for p in uncompleted)
            continue

        # Pick shortest burst (Tie-break: Arrival, then PID)
        next_p = min(available, key=lambda x: (x['bst'], x['arr'], x['pid']))

        start = time
        time += next_p['bst']
        gantt.append(f"{next_p['pid']}@{start}-{time}")

        tat = time - next_p['arr']
        total_tat += tat
        total_wait += (tat - next_p['bst'])
        completed.append(next_p)

    print("ALG SJF")
    print("GANTT " + " ".join(gantt))
    print(f"OK: AVG_WAIT {total_wait / n:.2f} AVG_TAT {total_tat / n:.2f}")


def main():
    input_data = sys.stdin.read().strip().split('\n')
    procs = []
    for line in input_data[1:]:
        if not line: continue
        parts = line.split(',')
        procs.append({'pid': parts[0].strip(), 'arr': int(parts[1]), 'bst': int(parts[2])})

    solve_fcfs(list(procs))
    solve_sjf(list(procs))


if __name__ == "__main__": main()



#printf "pid,arrival,burst\nP1,0,5\nP2,2,2\nP3,4,1" | python3 schedsim1.py