# Функция которая проверяет можно ли выиграть за m ходов
# S - Кол-во камней в кучею C - кол-во ходов выполненных в процессе игры. M - порог
# M нечетное - первый игрок (Петя). M четное - второй игрок (Ваня)
def f(s, c, m):
    # Если игра окончена, то кол-во ходов должно иметь ту же четность, что и m
    if s >= 30: return c % 2 == m % 2
    # Если игра не окончилась за M ходов - забиваем
    if c == m: return 0

    # Смотрим следующие ходы. Переписываем усовия из задачи
    h = [f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s * 2, c + 1, m)]

    # Если это ход целевого игрока, то достаточно победы в одном из вариантов
    # Иначе победа должна быть во всеч вариантов
    # Если в условие есть формлуировка 'Петя выиграл после неудачного/первого хода Вани', то all меняем на any
    # Если в условие есть формулирвка, что кто-то выиграл при любом ходе кого-то, то оставляем any
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# Использование
for s in range(1, 30):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            print(s, m)
            break