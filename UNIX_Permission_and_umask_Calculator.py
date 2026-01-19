def print_symbolic(mode):
    perms = "rwxrwxrwx"
    symbolic_str = ""

    for i in range(9):
        if mode & (1 << (8 - i)):
            symbolic_str += perms[i]
        else:
            symbolic_str += "-"
    print(symbolic_str)
def main():
    try:
        umask_input = input("Enter umask value (e.g., 022 or 002): ")
        umask_val = int(umask_input, 8)
    except ValueError:
        print("Invalid input. Please enter a valid octal number.")
        return

    dir_default = 0o777
    file_default = 0o666

    dir_result = dir_default & (~umask_val)
    file_result = file_default & (~umask_val)

    print(f"\nFor umask: {umask_val:03o}")

    print("New Directory Permissions:")
    print(f"  Octal: {dir_result:03o}")
    print("  Symbolic: ", end="")
    print_symbolic(dir_result)
    print("\n")

    print("New File Permissions:")
    print(f"  Octal: {file_result:03o}")
    print("  Symbolic: ", end="")
    print_symbolic(file_result)

if __name__ == "__main__":
    main()