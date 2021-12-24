#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('hey')
print('Aji',3)


# In[3]:


t='star'
type(t)


# In[10]:


print(int(5.7))
float(5)
a='56345'
print(int(a))


# In[12]:


4.5//2


# In[14]:


print(5/2)
print(5//2)


# In[17]:


7%10


# In[21]:


#logical operators along with conditional statements
a=2
if a==2 and a >3:
    print("yeah")
elif a==2 or a>3:
    print('oh')
else:
    print('ahh')


# In[23]:


#conversion of integer to binary
bin(100)


# In[26]:


#to convert binary to integer
int('1001010',2)


# In[5]:


22%4


# In[35]:


#membership operators
a='korea is pretty'
print('pretty' in a)
print('alia' in a)
print('bindhu' in 'bindhu alia')


# In[38]:


#identity operators is and is not
a=10
b=a
c=10
print (a is b)
print (c is not b)


# In[41]:


#getting input from user
a=input('enter any string')
print(a)
# to take numbers as input
a=int(input('enter any number'))
print(a)


# In[4]:


p=int(input('enter no of persons'))
g=int(input('enter no of gifts'))
if g%p==0:
    print("equally distributed")
else:
    b=g%p
    print('no of gifts needed',p-b)
    


# In[19]:


u='Alia'
p='Keo123'
a=input('enter user name')
if (u==a):
    b=int(input("enter any number"))
    if b%11==0:
        c=input('enter password')
        if(p==c):
            print('successful login')
        else:
            print('invalid details')
    else:
        print('invalid key')
else:
        print('invalid user')



# In[5]:


n=int(input('enter any number'))
c=0
s=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
        s=s+i
print('count is ',c)
print('sum is ',s)        
    


# In[6]:


n=int(input('enter any number'))
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if (c==2):
    print('prime number')


# In[7]:


n=int(input('enter any number'))
c=0
s=0
for i in range(1,n):
    if n%i==0:
        c=c+1
        s=s+i
print('count is ',c)
print('sum is ',s)  
if s==n:
    print('perfect number')


# In[11]:


n=int(input('enter any number'))
c=0
s=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
        s=s+i
print('count is ',c)
print('sum is ',s)   
if s-n==n:
    print('perfect number')
if (c==2):
    print('prime number')


# In[15]:


n=int(input('enter a number'))
s=0
c=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
    c=c+1
print(s)
print(c)


# In[1]:


n=(input('enter a number'))
c=len(n)
n=int(n)
s=0
while n>0:
    r=n%10
    print(c*r,end=' ')
    s=s*10+r
    n=n//10
    


# In[ ]:





# In[ ]:




