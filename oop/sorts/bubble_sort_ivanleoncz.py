
numbers = [19, 2, 31, 45, 6, 11, 121, 27]
sort_job_id = 1

print("Numbers:", numbers, "\n")
while True:
    permutations = 0
    for idx in range(0, len(numbers)):
        last_index = len(numbers) - 1
        if idx != last_index:
            if numbers[idx] > numbers[idx+1]:
                v = numbers.pop(idx)
                numbers.insert(idx+1, v)
                permutations += 1
    sort_job_id += 1
    print("Sort Job ID:", sort_job_id, "/ Permutations:", permutations)
    if sorted(numbers) == numbers:
        print("\nNumbers Sorted:", numbers)
        break
