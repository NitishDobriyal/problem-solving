def permutations(a, index, size, temp_set, final):
    if index == size:
        final.append(a.copy())
        return

    for i in range(index, size):
        if a[i] not in temp_set:
            temp_set.add(a[i])
            a[i], a[index] = a[index], a[i]

            permutations(a, index + 1, size, set(), final)

            a[index], a[i] = a[i], a[index]

    return final

a = [1, 1, 2]
temp_set = set()
final = []
print(permutations(a, 0, len(a), temp_set, final))

