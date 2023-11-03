heights = input("Input a list of student heights:\n ").split()
for n in range(0, len(heights)):
  heights[n] = int(heights[n]) #type:ignore
#a=sum(heights) (this can be a substitute for line 5,6,7)
a=0
for sum in heights:
  a+=sum #type:ignore
h=0
for total in heights:
  h += 1
print(f"avg height in students :{round(a/h)}")