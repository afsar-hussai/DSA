hash1=set()

print(f"Before adding in set: {hash1}")

hash1.add(5)
hash1.add(4)
hash1.add(3)
hash1.add(2)

print(f"After adding in set: {hash1}")

# to find a value

if 5 in hash1:
    print(True)

# to remove a value

if 2 in hash1:
    # even though it will not raise any error for saftey use if.
    hash1.discard(2)


