class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def success(content) -> None:
    print(colors.OKGREEN + f"[+] " + colors.ENDC + f"{content}")

def warning(content) -> None:
    print(colors.WARNING + f"[+] " + colors.ENDC + f"{content}")

def primary(content) -> None:
    print(colors.OKBLUE + f"[+] " + colors.ENDC + f"{content}")

def full_success(content) -> None:
    print(colors.OKGREEN + f"[+] {content}" + colors.ENDC)
