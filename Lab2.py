def display_main_menu():
    print("display_main_menu")

def get_user_input():
    temp = input("Enter some temperature values, separated by spaces: ")
    temp = temp.split()
    temp = [float(i) for i in temp]
    return temp

def calc_average(temp_list):
    if len(temp_list) == 0:
        return 0
    return sum(temp_list) / len(temp_list)

def find_min_max(temp_list):
    if len(temp_list) == 0:
        return 0, 0 
    return min(temp_list), max(temp_list)

def sort_temperature(temp_list):
    temp_list.sort()
    return temp_list

def calc_median_temperature(temp_list):
    temp_list.sort()
    if len(temp_list) % 2 == 0:
        return (temp_list[len(temp_list)//2] + temp_list[len(temp_list)//2-1]) / 2
    else:
        return temp_list[len(temp_list)//2]

temp_list = get_user_input()
average = calc_average(temp_list)
min_temp, max_temp = find_min_max(temp_list)
sorted_list = sort_temperature(temp_list)
median = calc_median_temperature(temp_list)

#print all the results in the console
print("\nAverage temperature:", average)
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)
print("Median temperature:", median)
print("Sorted temperature list:", sorted_list)