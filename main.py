def find_max(arr: list[int], max_sum: int):
    res: int = arr[0]

    for i in range(len(arr)):
        currSum: int = 0

        for j in range(i, len(arr)):
            currSum = currSum + arr[j]

            res = max(res, currSum)

    print(res)


def find_subarr(arr: list[int], max_sum: int):
    res_start = 0
    res_end = 0

    for i in range(len(arr)):

        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]

            if curr_sum > max_sum:
                res_start = i
                res_end = j

    res = []
    for i in range(res_start, res_end):
        res.append(arr[i])

    return res


list_one: list[int] = [1, -2, 3, 4, -1, 2, 1, -5, 4]
max_one: int = 9

list_two: list[int] = [2, 3, -2, 4]
max_two: int = 6


if __name__ == "__main__":
    find_max(list_one, max_one)

    res = find_subarr(list_two, max_two)
    for num in res:
        print(num, end=" ")
    print()
