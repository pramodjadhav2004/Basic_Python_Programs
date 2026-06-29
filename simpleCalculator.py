strr = input("Enter an expression (e.g., 5 + 3): ").split()
ans = 0
if strr[1] == "+":
    ans = int(strr[0]) + int(strr[2])
    print(ans)
elif strr[1] == "-":
    ans = int(strr[0]) - int(strr[2])
    print(ans)
elif strr[1] == "*":
    ans = int(strr[0]) * int(strr[2])
    print(ans)
elif strr[1] == "/":
    ans = int(strr[0]) / int(strr[2])
    print(ans)
elif strr[1] == "%":
    ans = int(strr[0]) % int(strr[2])
    print(ans)