#URL:https://www.hackerrank.com/challenges/balanced-brackets/problem?h_r=profile

def check_close(top, ch):
    if ch =="(" and top ==")":
        return True
    if ch =="[" and top =="]":
        return True
    if ch =="{" and top =="}":
        return True
    return False


def isBalanced(s):
    stack=[]
    for ch in s:
        #print("stack = ",stack)
        if  ch == "(" or ch == "[" or ch =="{":
            stack.append(ch)
        else:
            #print("in")
            stop = ""
            if stack:
                stop = stack.pop()
            else:
                return "NO"
            if not check_close(ch, stop):
                return "NO"
    if stack:
        return "NO"
    return "YES"
