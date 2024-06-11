n=int(input())
nums=list(map(int, input().split()))[:n]
def Bublesort(nums):
    n=len(nums)
    pos=n-1
    while pos>0:
        for i in range(0,pos):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            print(nums)
        pos-=1
Bublesort(nums)
print("after sorting",nums)