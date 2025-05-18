
#Lab solution for Week 12 Lab

#------------------------------------------
# Task 1
#------------------------------------------
import random
def data_generator(size):
    data = []
    for i in range(size):
        data.append(random.random())

    writefile = open("data.txt", "w")
    for item in data:
        writefile.write(str(item))
        writefile.write("\n")
    writefile.close()


#------------------------------------------
# Task 2
#------------------------------------------

def data_extractor():
    data_list = []
    readfile = open("data.txt","r")

    for line in readfile:
        data_list.append(float(line))

    readfile.close()
    return data_list


#------------------------------------------
# Task 3
#------------------------------------------
def find_max(data_list):
    largest  = data_list[0]
    for item in data_list:
        if item > largest:
            largest = item
    return largest
#------------------------------------------
# Task 4
#------------------------------------------
def main():
    data_generator(5)
    data = data_extractor()
    print("printing data list")
    print(data)

    print("printing largest value in data list")
    print(find_max(data))

main()



