def count_paths(F):

    # initialize the size, and two memorization tables, T and T2

    n = len(F)
    T = [[0 for i in range(n)] for i in range(n)]
    T2 = [[0 for i in range(n)] for i in range(n)]

    # base case (at T[-1][-1])
    # if there is a mushroom, we should add it, otherwise it should be blank (given there is a path)
    if F[-1][-1] == "m":

        T[-1][-1] = 1

    # base case for T2, where there exists a path
    T2[-1][-1] = 1

    # loop through all n^2 elements in T and T2, where T[-y][-x] and T2[-y][-x] represents the value at (-x, -y) respectively
    for y in range(1, n + 1):

        for x in range(1, n + 1):

            # ignore (-1, -1) since we defined base case
            if x == 1 and y == 1:
                continue

            # if we are at bottom row or right-most column, the elements below and the elements to the right respectively, should not exist (so defined as -inf)
            if x == 1:
                right = -float("inf")
            else:
                right = T[-y][-x + 1]
            if y == 1:
                down = -float("inf")
            else:
                down = T[-y + 1][-x]

            tile = F[-y][-x] # define tile

            # depending on if the tile is a tree, mushroom, or blank
            if tile == "t":
                T[-y][-x] = -float("inf")
            if tile == "m":
                T[-y][-x] = 1 + max(right, down)
            if tile == "x":
                T[-y][-x] = max(right, down)

            # solving for T2 is defined as if down and right are the same value, then that must mean there exists another path to the end
            if right == down and down != -float("inf"):

                T2[-y][-x] = T2[-y][-x + 1] + T2[-y + 1][-x]
            else:

                # finds which direction is the max mushroom direction
                mushrooms = max(right, down)
                if right == mushrooms:

                    T2[-y][-x] = T2[-y][-x + 1]
                else:

                    T2[-y][-x] = T2[-y + 1][-x]

    return T2[0][0]
