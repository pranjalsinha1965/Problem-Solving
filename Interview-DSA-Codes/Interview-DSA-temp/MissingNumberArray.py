def missing_number(a, N):
    for i in range(1, N+1):
        flag = 0

        for j in range(len(a)):
            if a[j] == i:
                flag = 1 
                break 
        
        if flag == 0:
            return i
        
    return -1

def main():
    N = 5 
    a = [1, 2, 4, 5]
    ans = missing_number(a, N)
    print("The missing number is: ", ans)

if __name__ == '__main__': 
    main()
