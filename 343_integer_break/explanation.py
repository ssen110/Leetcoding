if we look into the porblem correctly, then we can see that the maximum product will appear when the numbers are close to 
each other and the numbers are less.
means, 
	n = 10:
		nums1 = [1, 9] = 1*9 = 9
		nums2 = [2, 2, 2, 2, 2] = 32
                nums3 = [3, 3, 3, 1] = 27
                nums4 = [3, 3, 4] = 36 // here we can the see that the numbers are less and they are close to each other

To get nums4 = [3, 3, 4]
    len(nums4) = 3, 
    i.e, if we have k = 3
        len(nums4) = n // k = 10 // 3 = 3
        and there will be reminder = 1, 
        we can just add it with the first element. so the numbers become [4, 3, 3]

*** Code logic  ****
n 
res = 0
loop k from 2 to n :
    divi = n // k
    reminder = n % k
    temp = 1
    for i in range(n):
        if reminder:
            temp = temp * (divi + 1)
        else:
            temp = temp * divi

    res = max(res, temp)

return res

'''
    Note: We can improve the logic in 
               
    for i in range(n):
        if reminder:
            temp = temp * (divi + 1)
        else:
            temp = temp * divi
     
     as we extactly know the there is 1 increase for exactly reminder times
     we can just do it using power
        temp = pow(divi + 1, reminder) * pow(divi, k - reminder) 
        # n = 10, k = 3, reminder = 1, then k - reminder = 2, as 3 will appear 2 times
        
'''


    


		
