# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    bin = (format(N, 'b'))
    gap = 0
    max_gap = 0

    for items in bin:
        if items == '0':
            gap += 1

        if items == '1':
            if (gap > max_gap):
                max_gap = gap
                gap = 0

    return max_gap

# when submit the code, remove or comment out any print statement 
print(solution(9))
# output will be 2 
