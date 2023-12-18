'''this is used to find prim no '''
def answer(c):
    '''this is used to find prim no'''
    k = int(c ** (0.5))
    l = []
    for i in range(1, k + 1):
        if c % i == 0:
            l.append(i)

    result = [int(c / i) for i in l]
    l.extend(result)

    prim = []
    for j in l:
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            prim.append(j)

    return max(prim)


if __name__ == "__main__":
    print(answer(600851475143))
