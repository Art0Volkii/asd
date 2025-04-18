priority = {'+': 1, '-': 1, '*': 2, '/': 2}

def to_infix(prefix):
    stack = []

    for ch in reversed(prefix):
        if ch.isalpha():
            stack.append((ch, 3))
        else:
            left, p_left = stack.pop()
            right, p_right = stack.pop()
            curr_p = priority[ch]

            if p_left < curr_p:
                left = f'({left})'
            if p_right < curr_p or (ch in "-/" and p_right == curr_p):
                right = f'({right})'

            seq = f'{left}{ch}{right}'
            stack.append((seq, curr_p))
    return stack[0][0]

prefix = input().strip()
print(to_infix(prefix))

#RES: 100%
