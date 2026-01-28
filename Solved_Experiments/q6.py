import os, sys, signal, argparse

child_pid = 0
def handler(signum, frame):
    if child_pid: os.kill(child_pid, signal.SIGKILL)
    print("OK: TIMEOUT KILLED")
    sys.exit(0)

def main():
    global child_pid
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--seconds', type=int); parser.add_argument('--cmd'); parser.add_argument('--args')
    args = parser.parse_args()

    signal.signal(signal.SIGALRM, handler)
    child_pid = os.fork()
    if child_pid == 0:
        argv = [args.cmd] + (args.args.split(',') if args.args else [])
        os.execvp(args.cmd, argv)
    else:
        signal.alarm(args.seconds)
        _, status = os.waitpid(child_pid, 0)
        signal.alarm(0)
        if os.WIFEXITED(status): print(f"OK: EXIT {os.WEXITSTATUS(status)}")

if __name__ == "__main__": main()


# # Should kill process
# python3 timeoutwrap.py --seconds 1 --cmd /bin/sleep --args 5
# # Should exit normally
# python3 timeoutwrap.py --seconds 3 --cmd /bin/echo --args hi