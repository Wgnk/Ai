print("q1")
l1=list('hello')
print(l1)
print(len(l1))

print("q2")
t=('w','e','e','k')
l2=list(t)
print(l2)

print("q3")
l1=list(input("enter list elements"))
print(l1)

print("q4")
#
var1=int(input("enter value"))
# input 15+3 output 18, class int
print(var1,type(var1))

print("q5")
vowel=['a','e','i','o','u']
print(vowel[0])
#print(vowel(-1))
# -1 is u

print("q6")
vowel=['a','e','i','o','u']
for a in vowel:
    print(a)


print("q7")
vowel=['a','e','i','o','u']
length=len(vowel)
for a in range(length):
    print(a)

print("q8")
l1,l2=[1,2,3],[1,2,3]
l3=[1,[2,3]]
print(l1==l2)
print(l1==l3)
#print(l1<l3)
#print(l1<l2)


print("q9")
l1=[1,2]
l2=[3,4]
print(l1+l2)

print("q10")
print(l1)
print(l1*2)


print("q11")
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1[0:10:2])
#print[l1[::2]]
print(l1[5::2])
l2=l1.copy()
print(l2)

l2[0]+=10
print(l2)
print(l1.index(3))
l1.append(11)
print(l1)
l1.extend(l2)
print(l1)

l1.append([12,14])
print(l1)
print(len(l1))
l1.extend([16,18])
print(l1)
# extend append more than 1 value
l1.insert(1,50)
print(l1)

# pop remove the position from the list
print(l1.pop(0))
print(l1)
print(l1.pop(0))
# clear will remove sall items fro the list l1.clear()

print(l1.reverse())
#l3=sorted(l1,reverse=true))
print(l3)
#l3=sorted(l1)
print(l3)

print("==========================")
print("q12")
print(min(l1))
print(max(l1))
print(sum(l1))
# sorted created a new version whereas sort only sorts
# to delete an element
print(l1.pop(2))
# delete a p[articular element from the list
del l1[10]
print(l1)