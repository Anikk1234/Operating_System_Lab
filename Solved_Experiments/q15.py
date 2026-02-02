import sys


def main():
    data = sys.stdin.read().split()
    if not data: return
    P, E = int(data[0]), int(data[1])
    adj = {i: [] for i in range(P)}

    idx = 2
    for _ in range(E):
        u, v = int(data[idx]), int(data[idx + 1])
        adj[u].append(v)
        idx += 2

    visited = [False] * P
    stack = [False] * P
    cycle = []

    def dfs(u, path):
        visited[u] = True;
        stack[u] = True;
        path.append(u)
        for v in sorted(adj[u]):
            if not visited[v]:
                if dfs(v, path): return True
            elif stack[v]:
                # Cycle found
                cycle.extend(path[path.index(v):] + [v])
                return True
        stack[u] = False;
        path.pop()
        return False

    for i in range(P):
        if not visited[i]:
            if dfs(i, []):
                print("OK: DEADLOCK YES")
                print("OK: CYCLE " + " ".join(map(str, cycle)))
                return

    print("OK: DEADLOCK NO")


if __name__ == "__main__": main()



#printf "3 3\n0 1\n1 2\n2 1" | python3 wfgcheck.py