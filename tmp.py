

class Student:
    def __init__(self, fn, ln, age):
        self.fn = fn
        self.ln = ln
        self.age = age


'''
fn | ln | age
a  | b  | 28
'''

st = Student('a', 'b', 28)

print(st.age)
print(st.fn)
