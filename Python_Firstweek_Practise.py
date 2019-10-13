#!/usr/bin/env python
# coding: utf-8

# In[1]:


Name = "manish rai"

print(Name)
print(Name.title())
print(Name.upper())
print(Name.lower())


# In[14]:


First_Name = "manish "
Last_Name = " rai"
full_name = f"{First_Name}{Last_Name}"
print(full_name)
print(f"Hello,{full_name}")


# In[25]:


full_name = " manish "

print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())
print("\t Manish")


# In[31]:


print("fav_lang:\n\tpython\n\tjava\n\tdotnet")


# In[58]:


# How to use List

Students = ["Manish", "Shubham", "Amit"]
print(Students)
print(Students[1])
print(f"You are doing gud job,{Students[1].upper()}")

Students.append("Ashok")
print(Students)

Students.insert(2,"Mohit")
print(Students)
del Students[0]
print(Students)

Students.pop()
print(Students)

Students.pop(2)
print(Students)


# In[68]:


cars = ["bmw", "audi", "toyta", "benz"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
len(cars)


# In[84]:


##For Loop

Students = ["Manish", "Shubham", "Mohit", "Amit", "Ashok"]
for student in Students:
    
    
    print(f"{student.title()}, Keep up the Good Work")


# In[ ]:




