def steepest_ascent(a):
    i = 0

    while i < len(a) - 1:
        best = i

        for j in range(i + 1, len(a)):
            if a[j] > a[best]:
                best = j

        if best == i:
            break

        i = best

    print("Best value:", a[i])


a = [1, 3, 5, 7, 6, 4, 2, 8, 9, 5]
steepest_ascent(a)