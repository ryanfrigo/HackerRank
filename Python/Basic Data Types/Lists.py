if __name__ == '__main__':
    N = int(input())

lst = []

for i in range(0, N):
    command = input().split()
    if command[0] == "print":
        print(lst)
    else:
        eval("lst." + command[0] + "(" + ",".join(command[1:]) + ")")
