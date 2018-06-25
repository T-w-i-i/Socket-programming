# client.py

import socket
import pickle

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
soc.connect(("127.0.0.1", 12345))

## Asking about the name 
question_name_bytes = soc.recv(9192) # the number means how the response can be in bytes  
question_name_string = question_name_bytes.decode("utf8") # the return will be in bytes, so decode
name = input(question_name_string)
soc.send(name.encode("utf8")) # we must encode the string to bytes  


## Asking about the admission number
question_admission_bytes = soc.recv(9192)
question_admission_string = question_admission_bytes.decode("utf8")
admission = input(question_admission_string)
soc.send(admission.encode("utf8"))


## Asking course
question_course_bytes = soc.recv(9192)
question_course_string = question_course_bytes.decode("utf8")
course = input(question_course_string)
soc.send(course.encode("utf8"))

## Asking faculty
question_faculty_bytes = soc.recv(9192)
question_faculty_string = question_faculty_bytes.decode("utf8")
faculty = input(question_faculty_string)
soc.send(faculty.encode("utf8"))

##the code
question_code_bytes = soc.recv(9192)
question_code_string = question_course_bytes.decode("utf8")
Coderesent = input(question_code_string)
soc.send(Coderesent.encode("utf8"))

final_response = soc.recv(100000000)
print(final_response.decode("utf8"))

