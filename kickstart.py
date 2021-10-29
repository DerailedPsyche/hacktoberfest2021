test_cases = int(input())
for i in range(test_cases):
    days,number_of_lines,max_rides = input().split(" ")
    relation = {}
    largest_sum = 0 
    for j in range(int(number_of_lines)):
        h,s,e = input().split(" ")
        relation[int(h)] = set([x for x in range(int(s),int(e)+1)])
    arr = [int(x) for x in relation.keys()]
    arr = sorted(arr,reverse=True)
    for k in range(1,int(days)+1):
        happy_sum = 0
        count = 0
        for l in arr:
            if(k in relation[l] and count<int(max_rides)):
                happy_sum += l
                count += 1  
        if(happy_sum>largest_sum):
            largest_sum = happy_sum
    print(f"Case #{i+1}: {largest_sum}")
    
            