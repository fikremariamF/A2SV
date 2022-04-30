def theatreSquare():
	nums=input().split()
	s1=int(nums[0])
	s2=int(nums[1])
	a=int(nums[2])
	width=s1/a if s1%a==0 else s1//a+1
	height=s2/a if s2%a==0 else s2//a+1
	return int(width*height)
print(theatreSquare())
