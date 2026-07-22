def quick_sort(a):
    return a if len(a)<=1 else quick_sort([x for x in a[1:] if x<=a[0]])+[a[0]]+quick_sort([x for x in a[1:] if x>a[0]])
