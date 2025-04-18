BRACKETS = {"(":")", "[":"]", "{":"}"}

def check(seq: str):
    stack = []
    for brack in seq:
        if brack in BRACKETS:
            stack.append(brack)
        else:
            if len(stack) == 0 or BRACKETS.get(stack.pop()) != brack:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            res = check(line)
            print("yes" if res else "no")


#RES: 100%
