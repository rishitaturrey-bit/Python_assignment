
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

print("Total items:", len(nums))
print("Last item:", nums[-1])
print("Reversed tuple:", nums[::-1])

if 5 in nums:
    print("Yes, 5 is present")
else:
    print("No, 5 is not present")

if len(nums) > 2:
    new_tuple = tuple(sorted(nums[1:-1]))
    print("After removing first & last and sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last")


