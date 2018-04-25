# Be careful of things that are secretly pointers...

a = [{}] * 3
a[0]['k'] = 'v'
print(a)
# [{'k': 'v'}, {'k': 'v'}, {'k': 'v'}]

# But
a = [None] * 3
a[0] = 1
print(a)
# [1, None, None]

# Only way I know to avoid this is with a list comprehension
a = [{} for i in range(3)]
a[0]['k'] = 'v'
print(a)
# [{'k': 'v'}, {}, {}]
