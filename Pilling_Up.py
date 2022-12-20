l,r = 0, len(block)-1
    prev = float("inf")
    print(block)
    while l <= r:
        print(l,r)
        if block[l] <= prev and block[l] >= block[r]:
            prev = block[l]
            print(prev)
            l += 1
        elif block[r] <= prev and block[r] >= block[l]:
            prev = block[r]
            print(prev)
            r -= 1
        elif prev > block[r] or prev > block[l]:
            print("No")
            break
