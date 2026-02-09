sample_bay=["Basalt","Silica","Iron","Dust"]
print(sample_bay[0])
print(sample_bay[len(sample_bay)-1])
#first element in sample_bay list is numbered at 0/zero. so the four elements are numbered 0 to 3 respectively. to print the last element we say count the number of elements 1,2,3,4 then subtract 1 this gives 3 now find the element numbered at this number (find the 3rd element in the list). sample_bay goes before so we now which list we are using.
print(len(sample_bay))
# here we just ask to print number of elements in sample_bay list



sample_bay=[{"Sample Name":"Basalt"},{"Sample Name":"Silica"},{"Sample Name":"Iron"},{"Sample Name":"Dust"}]
for sample in sample_bay:
    print(f"Transmitting data for: {sample['Sample Name']}") #sample_bay is the list of text book you have available, sample in the specific name of each textbook, Sample Name is the topic/ chapter in the textbook you want to read. so we listed sample_bay a.k.a we have out all the possible textbooks we can search. we then say we want the maths one a.k.a sample, which topic- Sample Name.

new_finding=[]#empty list is here
for n in range(3):# repaet 3 times these instructions
    rock=input("New rock is? ")#input
    new_finding.append(rock)# to the empty list, add the input
print(new_finding)#outside of loop the result of above instructions 
    
    
sample_bay=["Basalt","Silica","Iron","Dust"]
if "Dust" in sample_bay:
    print("Dust found")
else:
    print("Dust not found")
sample_bay.remove("Dust")
print(sample_bay)
OR
try:
    where = sample_bay.index("Dust")
    print(f"Found 'Dust' at index {where}")
except ValueError:
    print("'Dust' not found in the list")
else:
    sample_bay.remove("Dust")
    print(sample_bay)