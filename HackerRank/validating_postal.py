def inn(p):
    return 100000 <= int(p) <= 999999


def imm(p):
    l = []
    for i in range(len(p) - 2):
        l.append(p[i] != p[i + 2])

    return all(l)


def is_valid(p):
    return (p.isdigit() and inn(p)) and (p != "110000")# and imm(p)


def main():
    p = input()
    print(is_valid(p))
    
    
main()
