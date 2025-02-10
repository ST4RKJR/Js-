def recurse(nums,i):
    if i >= len(nums):
        return 0

    chori_karo = nums[i] + recurse(nums,i+2)
    abhi_chori_mat_karo = 0 + recurse(nums,i+1)
    return max(chori_karo,abhi_chori_mat_karo)



def rob(nums):      
    # if nums[i] >= n : 
    #     return 0
    # if 
    return recurse(nums,0)



#Time Complexity of this code will be O(2^n)
#Space Complexity of this code will be