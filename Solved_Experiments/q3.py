import os, sys, argparse, stat

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--path'); parser.add_argument('--sort', default='name')
    args = parser.parse_args()

    if not args.path or not os.path.isdir(args.path):
        print("ERROR: E_NOTDIR: invalid directory"); sys.exit(1)

    entries, counts = [], {'F':0, 'D':0, 'L':0, 'O':0}
    try:
        for name in os.listdir(args.path):
            st = os.lstat(os.path.join(args.path, name))
            etype = 'F' if stat.S_ISREG(st.st_mode) else 'D' if stat.S_ISDIR(st.st_mode) else 'L' if stat.S_ISLNK(st.st_mode) else 'O'
            counts[etype] += 1
            entries.append({'type': etype, 'size': st.st_size, 'name': name})
    except: print("ERROR: E_READ"); sys.exit(1)

    entries.sort(key=lambda x: (x['size'], x['name']) if args.sort == 'size' else x['name'])
    for e in entries: print(f"ENTRY {e['type']} {e['size']} {e['name']}")
    print(f"OK: TOTAL {len(entries)} FILES {counts['F']} DIRS {counts['D']} LINKS {counts['L']} OTHER {counts['O']}")

if __name__ == "__main__": main()

#python3 dirreport.py --path . --sort name