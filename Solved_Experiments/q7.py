import os, sys


def main():
    r1, w1 = os.pipe()
    r2, w2 = os.pipe()

    if os.fork() == 0:  # Producer (echo hello)
        os.dup2(w1, 1);
        os.close(r1);
        os.close(w1);
        os.close(r2);
        os.close(w2)
        os.execlp("echo", "echo", "hello")

    if os.fork() == 0:  # Filter (tr a-z A-Z)
        os.dup2(r1, 0);
        os.dup2(w2, 1);
        os.close(r1);
        os.close(w1);
        os.close(r2);
        os.close(w2)
        os.execlp("tr", "tr", "a-z", "A-Z")

    if os.fork() == 0:  # Consumer (wc -c)
        os.dup2(r2, 0);
        os.close(r1);
        os.close(w1);
        os.close(r2);
        os.close(w2)
        os.execlp("wc", "wc", "-c")

    os.close(r1);
    os.close(w1);
    os.close(r2);
    os.close(w2)
    os.wait();
    os.wait();
    os.wait()
    print("OK: PIPELINE SUCCESS")


if __name__ == "__main__": main()





# python3 pipechain.py