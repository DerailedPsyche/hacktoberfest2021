test_dict = {'gfg' : [5, 6, 7, 8], 
             'is' : [10, 11, 7, 5], 
             'best' : [6, 12, 10, 8], 
             'for' : [1, 2, 5]} 
  
print("The original dictionary is : " + str(test_dict)) 
  
res = list(sorted({ele for val in test_dict.values() for ele in val}))  
print("The unique values list is : " + str(res)) 
