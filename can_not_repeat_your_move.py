# Нельзя повторять свой прошлый ход

def f(s, p0, p1, c, m):
    if s >= 21: return c % 2 == m % 2
    if c == m: return 0

    h = []
    if p1 != '+1': h += [f(s + 1, '+1', p0, c + 1, m)]
    if p1 != '+2': h += [f(s + 2, '+2', p0, c + 1, m)]
    if p1 != '*2': h += [f(s * 2, '*2', p0, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 20):
    for m in range(1, 6):
        if f(s, '', '', 0, m) == 1:
            print(s, m)
            break