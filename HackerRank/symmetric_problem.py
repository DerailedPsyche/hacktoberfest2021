# Problem Link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
if n > 0 and n < 1000:
    nn = input().split()
    if len(nn) < (n + 1):
        stamp_n = [int(num) for num in nn]
    else:
        raise Exception("Sorry total student number not matching roll in English")
    #converted list into a set
    stamp_n_set = set(stamp_n)

else:
    raise Exception("Sorry number should be between 0 to 1000")

m = int(input())
if m > 0 and m < 1000:
    mm = input().split()
    if len(mm) < (m + 1):
        stamp_m = [int(num) for num in mm]
    else:
        raise Exception("Sorry total student number not matching roll in French")
    stamp_m_set = set(stamp_m)


else:
    raise Exception("Sorry number should be between 0 to 1000")

# difference between two set is found using symmetric_difference() function
symm_diff = stamp_n_set.symmetric_difference(stamp_m_set)

print(len(symm_diff))