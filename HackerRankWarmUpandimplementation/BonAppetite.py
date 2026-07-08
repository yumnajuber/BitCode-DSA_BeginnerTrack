def bonAppetit(bill, k, b):
    anna = (sum(bill) - bill[k]) / 2
    if b == anna:
        return "Bon Appetit"
    else:
        return b - anna

n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())
print(bonAppetit(bill, k, b))