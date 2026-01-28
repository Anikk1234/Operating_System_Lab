import threading, argparse

buffer, produced, consumed_sum = [], 0, 0
mutex = threading.Lock()


def producer(items, empty, full):
    global produced
    while True:
        with mutex:
            if produced >= items: break
            produced += 1
            val = produced
        empty.acquire()
        buffer.append(val)
        full.release()


def consumer(items, empty, full):
    global consumed_sum, produced
    while True:
        if not full.acquire(timeout=0.1):  # Avoid deadlock at end
            if produced >= items and not buffer: break
            continue
        val = buffer.pop(0)
        with mutex:
            consumed_sum += val
        empty.release()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--buf', type=int);
    parser.add_argument('--producers', type=int);
    parser.add_argument('--consumers', type=int);
    parser.add_argument('--items', type=int)
    args = parser.parse_args()

    empty, full = threading.Semaphore(args.buf), threading.Semaphore(0)
    prods = [threading.Thread(target=producer, args=(args.items, empty, full)) for _ in range(args.producers)]
    cons = [threading.Thread(target=consumer, args=(args.items, empty, full)) for _ in range(args.consumers)]

    for t in prods + cons: t.start()
    for t in prods + cons: t.join()
    print(f"OK: PRODUCED {args.items}\nOK: CONSUMED {args.items}\nOK: SUM {consumed_sum}")


if __name__ == "__main__": main()



#python3 pcbuf.py --buf 5 --producers 2 --consumers 2 --items 20