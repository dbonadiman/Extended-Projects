import sys

def merge(l,r):
    res = []
    while l+r:
        if l and r:
            if l[0]<r[0]:
                res.append(l.pop(0))
            else:
                res.append(r.pop(0))
        elif l:
            res += l
            l = []
        elif r:
            res += r
            r = []
    return res
            
def merge_sort(lis):
    if len(lis)<=1:
        return lis
    mid = int(len(lis)/2)
    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])
    return merge(left,right)
    
def bubble_sort(lis):
    while True:
        n = len(lis)
        sw = False
        for j in range(n-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
                sw = True
        n-=1
        if not sw:
            break  
    return lis
    
def main():
    lis = [2,4,1,7,6,4,9,0]
    print("List: {}".format(lis))
    print("Merge Sorted list: {}".format(merge_sort(lis)))
    print("Bubble Sorted list: {}".format(bubble_sort(lis)))
    lis = []
    print("List: {}".format(lis))
    print("Merge Sorted list: {}".format(merge_sort(lis)))
    print("Bubble Sorted list: {}".format(bubble_sort(lis)))
    lis = [0]
    print("List: {}".format(lis))
    print("Merge Sorted list: {}".format(merge_sort(lis)))
    print("Bubble Sorted list: {}".format(bubble_sort(lis)))
    lis = [2,4,1]
    print("List: {}".format(lis))
    print("Merge Sorted list: {}".format(merge_sort(lis)))
    print("Bubble Sorted list: {}".format(bubble_sort(lis)))

if __name__=="__main__":
    status = main()
    sys.exit(status)