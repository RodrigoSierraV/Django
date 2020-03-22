def depth(array):
    """    long = len(array)
    if long == 0:
        return 1"""
    return max([depth(arr) for arr in array], default=0) + 1 

"""def depth2(array):
    for i in array:
        while len(i) != 0:"""

def depth2(array):
     buffer = [(0, array)]
     max_depth = 0
     while buffer:
         d, item = buffer.pop()
         print('Buffer after pop', buffer)
         max_depth = max(max_depth, d+1)
         print( 'max depth',max_depth)
         buffer.extend((d+1, child) for child in item)
         print('buffer after extend', buffer)
     return max_depth 

print(depth2([[[[]]], [[[[[[[[[[[[[]]]]]]]]]]]]]]))