#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        for letter in  my_string:
            if letter != 'c' or letter != 'C':
                print(letter, end='')
            else:
                print(end='')
no_c("can Copy")
