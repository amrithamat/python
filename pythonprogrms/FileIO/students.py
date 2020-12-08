#done by myself

"""f=open("students","r")
st=set()
f1=open("passed","r")
st1=set()
for lines in f:
    st.add(lines.rstrip("\n"))
print("names=",st)
for lines in f1:
    st1.add(lines.rstrip("\n"))
print("passed=",st1)
print("failed=",st-st1)"""


f=open("students","r")
f1=open("passed","r")
def convert_to_set(file):
    file_set=set()
    for names in file:
        file_set.add(names.rstrip('\n'))
    return file_set
students_set=convert_to_set(f)
students_passed=convert_to_set(f1)
print(students_set-students_passed)
