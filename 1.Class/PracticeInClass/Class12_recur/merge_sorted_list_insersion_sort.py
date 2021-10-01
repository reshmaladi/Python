#!C:\Python34

def mergeSortedList(l1,l2):
    i=j=0
    l3=[]
    while(i<len(l1) and j<len(l2)):
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    if(i<len(l1)):
        l3.extend(l1[i:])
    if(j<len(l2)):
        l3.extend(l2[j:])
    return l3

def main():
    l1=input("Enter first list: ")
    l2=input("Enter second list: ")
    print(mergeSortedList(l1,l2))

if __name__=='__main__':
    main()
