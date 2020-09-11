def solve(D, arr) -> int:
    storedStates = []
    for optionsConsidered in range(len(arr) + 1):
        storedStates.append([])
        for dollarsUsed in range(D+1):
            storedStates[-1].append(0)

    for option, row in enumerate(storedStates):
        for cost in range(len(row)):
            if option == 0 or cost == 0: row[cost] = 0
            elif arr[option-1][0] > cost: row[cost] = storedStates[option-1][cost]
            elif arr[option-1][0] <= cost: row[cost] = max(storedStates[option-1][cost],
            storedStates[option-1][cost - arr[option-1][0]] + arr[option-1][1])
    return storedStates[-1][-1]
