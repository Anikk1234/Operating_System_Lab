import multiprocessing, argparse


def worker(counter, lock, iters):
    for _ in range(iters):
        with lock: counter.value += 1


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--procs', type=int);
    parser.add_argument('--iters', type=int);
    parser.add_argument('--name')
    args = parser.parse_args()

    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    procs = [multiprocessing.Process(target=worker, args=(counter, lock, args.iters)) for _ in range(args.procs)]

    for p in procs: p.start()
    for p in procs: p.join()
    print(f"OK: FINAL {counter.value}")


if __name__ == "__main__": main()

#python3 shmcounter.py --procs 4 --iters 1000 --name test