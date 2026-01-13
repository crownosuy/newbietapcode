def S(n):
    if n == 0:
        return 0
    else:
        return n + S(n - 1)
if __name__ == "__main__":
    n =765
    print(S(456))


    
