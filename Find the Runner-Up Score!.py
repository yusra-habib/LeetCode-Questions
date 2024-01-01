#approach:used float('-inf')
#WHY?IF INPUT IS LIKE THIS 5 5 5 5 5 THEN THERE WILL BE NO RUNNERUP
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr=list(arr)#TOCONVERT '[1 2 3 4]' TO [1 2 3 4]
    first=max(list_arr)
    sec=float('-inf')
    for char in list_arr:
        if char<first and char>sec:
            sec=char
               
    print(sec)
