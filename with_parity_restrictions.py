# Удвоение камней разрешено, есло в куче на момент действия нечетное кол-во камней
def f(s, c, m):
    if s >= 22: return c % 2 == m % 2
    if c == m: return 0

    h = [f(s+1, c+1, m), f(s+2, c+1, m)]
    if s % 2 != 0: h += [f(s*2, c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)


for s in range(1, 22):
    for m in range(1, 6):
        if f(s, 0, m) == 1:
            if m == 5: print(s, m)
            break