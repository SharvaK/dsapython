def binary_search(list_num, first_index,last_index,to_search):
    if last_index >= first_index:
        mid_index = (first_index + last_index)//2
        mid_element = list_num[mid_index]


        if mid_element == to_search:
            return f"{mid_element} occurs at {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1 
            # new last index is new position
            return binary_search(list_num,first_index,new_position,to_search)

        elif mid_element < to_search:
            new_position = mid_index + 1        
            # new first index is new position
            return binary_search(list_num,first_index,last_index,to_search)

    else:
        return "Does not appear in list"


blist = [10,17,24,35,46,52,76] 
search = 17
first = 0
last = len(blist) - 1

print(binary_search(blist,first,last,search))
       
