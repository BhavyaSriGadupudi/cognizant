def binary_search(a,key):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==key:return m
        if a[m]<key:l=m+1
        else:r=m-1
    return -1
