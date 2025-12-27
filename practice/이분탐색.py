arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

# 찾을 값
target = 27
left, right = 0, len(arr) - 1
cnt =  0

print(f"시작값 : {left} 끝값 : {right}")
while(left <= right) :
    cnt += 1
    mid = (left + right) // 2
    if target == arr[mid] :
        break
    elif target < arr[mid] :
        right = mid - 1
    elif arr[mid] < target :
        left = mid + 1
    print(f"현재 mid : {mid}, 시도횟수 : {cnt}" )

