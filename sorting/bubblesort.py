import sys

def bubblesort(input_file):
    n=len(input_file)
    for i in range(n-1):
        for j in range(n-1-i):
            if input_file[j] > input_file[j+1]:
                input_file[j], input_file[j+1]=input_file[j+1], input_file[j]
    return input_file


def main():
    input_list=[5,2,0,6]
    print(bubblesort(input_list))

if __name__ == '__main__':
    main()
