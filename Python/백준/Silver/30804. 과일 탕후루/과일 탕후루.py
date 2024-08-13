n = int(input())
arr = list(map(int, input().split())) +[-1]

ans = 1
is_in = [0 for _ in range(10)]

start = 0
end = 0
is_in[arr[0]] += 1
while end < n:
    #print(10 - is_in.count(0))
    #print(arr[start:end + 1])
    if 10 - is_in.count(0) < 3:
        #print("end++")
        ans = max(ans, end - start + 1)
        end += 1
        is_in[arr[end]] += 1
    else:
        #print("start++")
        is_in[arr[start]] -= 1
        start += 1
    #print(f"ans = {ans}")
print(ans)