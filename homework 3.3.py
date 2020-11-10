def my_func(one,two,three):
    common_list=[one,two,three]
    max_number1=max(common_list)
    common_list.remove(max_number1)
    max_number2=max(common_list)
    return (max_number2+max_number1)

print(my_func(3,4,6))


