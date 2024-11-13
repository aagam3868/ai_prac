def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary, so they are out of the way
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks that we left on auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Number of disks
n = int(input("Enter the number of disks:"))

# Call the function with source as 'A', target as 'C', and auxiliary as 'B'
tower_of_hanoi(n, 'A', 'C', 'B')
