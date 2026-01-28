import threading, argparse

total_sum = 0
mutex = threading.Lock()


def worker(start, end):
    global total_sum
    local = sum(range(start, end + 1))
    with mutex: total_sum += local


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--threads', type=int);
    parser.add_argument('--n', type=int)
    args = parser.parse_args()

    chunk = args.n // args.threads
    threads = []
    for i in range(args.threads):
        s = i * chunk + 1
        e = (i + 1) * chunk if i < args.threads - 1 else args.n
        t = threading.Thread(target=worker, args=(s, e))
        threads.append(t);
        t.start()

    for t in threads: t.join()
    print(f"OK: SUM {total_sum}")


if __name__ == "__main__": main()

#python3 thrsum.py --threads 4 --n 100