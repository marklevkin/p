def drawn_bracket(names):
    from math import log, floor
    from random import choice
    if log(len(names), 2) != int(log(len(names), 2)):
        names += ["BYE"] * ((2 ** (int(log(len(names), 2)) + 1)) - len(names))
    g = int(log(len(names), 2))
    d = set()
    de = list(range(1, 2 ** g + 1))
    for s in range(1, 2 ** g + 1):
        if s > 1: fl = ((log(s - 1, 2)) % 1 == 0)
        if s == 1:
            x = [1]
        elif s == 2:
            x = [2 ** g]
        elif s == 3:
            x = [(3 * 2 ** g) / 4, (2 ** g) / 4 + 1]
        elif s == 5:
            x = [(2 ** g) / 4, (2 ** g) / 2, (2 ** g / 2) + 1, (3 * (2 ** g) / 4) + 1]
        elif 8 < s <= 2 ** (g - 2) and fl:
            k = floor(log(s, 2))
            x = [j for i in range(1, 2 ** k, 2) for j in (i * 2 ** g / (2 ** k), i * 2 ** g / (2 ** k) + 1)]
        elif s > 2 ** (g - 2) and fl:
            x = de.copy()
        c = choice(x)
        x.remove(c)
        c = int(c)
        de.remove(c)
        d.add((c, f'{c}:{names[s - 1]} ({s})') if s <= 2 ** (g - 2) else (c, f'{c}:{names[s - 1]}'))
    ans = [pl[1] for pl in sorted(d)]
    return ans


if __name__ == '__main__':
    for j in drawn_bracket([str(i) for i in range(16)]): print(j)




def fixed_bracket(names):
    from math import ceil, log
    n1 = len(names)
    if log(n1, 2) != int(log(n1, 2)):
        names += ["BYE"] * ((2 ** (int(log(n1, 2)) + 1)) - n1)
    n = 2 ** (int(log(n1, 2)) + 1)
    b = []
    for a in range(1, n + 1):
        if a == 1:
            s = 1
        else:
            c = ceil(log(a, 2)) - 1
            k = ((2 ** c) * 3 + 1) / 2
            k1 = abs(a - k)
            if k1 == 2 ** (c - 1) - 0.5:
                m = 1
            else:
                m = 2 * (k1 + 1)
            s = (m * 2 ** (log(n, 2) - c)) + a % 2
            s = int(s)
        b.append(str(a) + ' : ' + names[s - 1] + f' ({s})' if s <= n1 else str(a) + ' : ' + names[s - 1])
    return b


if __name__ == '__main__':
    for j in fixed_bracket(['v', 'kl', 'nd', 'fr', 'frt']): print(j)


#
def round_robin(names):
    d = {}
    if len(names) % 2 == 1: names.append('BYE')
    n = len(names) - 1
    m = (n + 1) // 2
    c = []
    a = [names[i - 1] for _ in range(m) for i in range(1, n + 1)]
    b = a[-n - 1::-1]
    for i in range(0, (n - 1) * (m - 1) + 1, m - 1):
        c.append(a.pop(i))
    s = tuple(zip(a, b))
    for i in range(n):
        if i % 2 == 0:
            d[i + 1] = (c[i], names[n]), *s[i * (m - 1):(i + 1) * (m - 1)]
        else:
            d[i + 1] = (names[n], c[i]), *s[i * (m - 1):(i + 1) * (m - 1)]
    return d


if __name__ == '__main__':
    for j, i in round_robin(['1', '2', '3', '4', '5', '6']).items():
        print(j, *[f'{k[0]}-{k[1]}' for k in i], sep='|     ')
