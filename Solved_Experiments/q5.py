import os, sys, argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--cmd');
    parser.add_argument('--args');
    parser.add_argument('--repeat', type=int, default=1)
    args = parser.parse_args()

    cargs = [args.cmd] + (args.args.split(',') if args.args else [])
    for i in range(1, args.repeat + 1):
        pid = os.fork()
        if pid == 0:
            try:
                os.execvp(args.cmd, cargs)
            except:
                sys.exit(127)
        else:
            print(f"CHILD {i} PID {pid} START")
            _, status = os.waitpid(pid, 0)
            if os.WIFEXITED(status):
                print(f"CHILD {i} PID {pid} EXIT {os.WEXITSTATUS(status)}")
            elif os.WIFSIGNALED(status):
                print(f"CHILD {i} PID {pid} SIG {os.WTERMSIG(status)}")
    print(f"OK: COMPLETED {args.repeat}")


if __name__ == "__main__": main()

# python3 spawnwait.py --cmd /bin/echo --args "Hello World" --repeat 2