from collections import deque

def solution(arr):
    n = len(arr)
    
    queue = deque([arr])
    nums = [0, 0]
    while queue:
        array = queue.popleft()
        #print(array)
        if len(array) == 1 or zip_possible(array):
            nums[array[0][0]] +=1
        else:
            dv_list = devide_into_four(array)
            queue.extend(dv_list)
    #print(nums)    
    return nums

def devide_into_four(array):
    n = len(array)
    
    list1 = [ele[:n//2] for ele in array[:n//2]]
    list2 = [ele[n//2:] for ele in array[:n//2]]
    list3 = [ele[:n//2] for ele in array[n//2:]]
    list4 = [ele[n//2:] for ele in array[n//2:]]
    
    return [list1, list2, list3, list4]
def zip_possible(arr):
    num = arr[0][0]
    
    for arr_ in arr:
        for cell in arr_:
            if cell != num:
                return False
            
    return True