#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx >= 0 and idx < len(my_list):
            new_list = []
            for num in my_list:
                new_list.append(num)
            for i in range(len(my_list) - 1):
                new_list[idx] = element
                return new_list
        else:
            return my_list


lis = [12, 33, 22, 44]
idx = 3
el = 66
print(new_in_list(lis, idx, el))
print(lis)
'''if __name__ == "__main__":
    new_in_list()'''
