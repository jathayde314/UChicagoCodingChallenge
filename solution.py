def solve(D, arr) -> int:
    storedStates = [[0 for dollarsUsed in range(0, D+1)] for optionsConsidered in range(0, len(arr) + 1)]

    for option, row in enumerate(storedStates):
        for cost in range(len(row)):
            if option == 0 or cost == 0: row[cost] = 0
            elif arr[option-1][0] > weight: row[cost] = storedStates[option-1][cost]
            elif arr[option-1][0] <= weight: row[cost] = max(storedStates[option-1][cost],
            storedStates[option-1][cost - arr[option-1][0]] + arr[option-1][1])
    return storedStates[-1][-1]
