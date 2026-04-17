def main():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the size of the array
        a = list(map(int, input().split()))  # Read the array elements

        even1, even2 = 0, 0
        odd1, odd2 = 0, 0
        
        for i in range(n):
            if i % 2 == 0:
                if a[i] % 2 == 1:
                    odd1 = 1
                else:
                    even1 = 1
            else:
                if a[i] % 2 == 1:
                    odd2 = 1
                else:
                    even2 = 1
        
        if even1 and odd1:
            print("NO")
        elif even2 and odd2:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()