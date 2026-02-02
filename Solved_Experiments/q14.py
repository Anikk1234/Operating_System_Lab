import sys


def main():
    lines = sys.stdin.read().strip().split('\n')
    lines = [l for l in lines if l.strip()]

    P, R = map(int, lines[0].split())
    alloc, max_req = [], []

    curr = 1
    for _ in range(P): alloc.append(list(map(int, lines[curr].split()))); curr += 1
    for _ in range(P): max_req.append(list(map(int, lines[curr].split()))); curr += 1
    avail = list(map(int, lines[curr].split()))

    need = [[max_req[i][j] - alloc[i][j] for j in range(R)] for i in range(P)]

    # Check invalid state
    for i in range(P):
        if any(need[i][j] < 0 for j in range(R)):
            print("ERROR: E_INVALID: allocation > max");
            sys.exit(1)

    work = avail[:]
    finish = [False] * P
    seq = []

    while len(seq) < P:
        found = False
        for i in range(P):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(R)):
                for j in range(R): work[j] += alloc[i][j]
                finish[i] = True
                seq.append(i)
                found = True
                break
        if not found:
            print("OK: UNSAFE");
            return

    print("OK: SAFE")
    print("OK: SEQ " + " ".join(map(str, seq)))


if __name__ == "__main__": main()


#printf "3 2\n1 0\n0 1\n1 1\n2 0\n1 2\n1 1\n1 1" | python3 banker.py