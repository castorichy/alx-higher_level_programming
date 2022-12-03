#!/usr/bin/python3
if __name__ == "__main__":
    def new_in_list(my_list, idx, element):
        new_list = []
        if idx > 0 and idx <= len(new_list):
            new_list.append(mylist[:])
            new_list[idx] = element
            return new_list
        else:
            return my_list


lst = [33, 45, 12, 77, 54]
idx = 4
elem = 900
print(new_in_list(lst, idx, elem))
print(lst)
