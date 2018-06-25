# server.py
import pickle
import random

def do_some_stuffs_with_input(input_string):  
    
    

    print("Processing the input")
    
    return input_string


def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 1000000):
    

    """questions = ["Name:", "Admission number:", "Faculty&Course:", "Code:"]
    for query in questions:
        if (query is "Code:"):
            Code = random.randint(1,100)
            conn.sendall("Your code is: {}. Please Resend it as a security check".format(Code).encode("utf8"))
   
        conn.sendall(query.encode("utf8"))
        answer = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
        print(answer)
       """
    conn.sendall("What is your name?\n".encode("utf8"))
    name = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
    print (name)
    conn.sendall("What is your admission number?\n".encode("utf8"))
    admission = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
    print (admission)
    conn.sendall("Input your Course\n".encode("utf8"))
    course = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
    print (course)
    conn.sendall("Input your faculty\n".encode("utf8"))
    faculty = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
    print (faculty)
    Code = random.randint(1,1000)
    conn.sendall("Your code is: {}. Please Resend it as a security check\n".format(Code).encode("utf8"))
    Coderesent = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
    print (Coderesent) 
    
    conn.sendall("""###############################Thank you for conecting with us.!!\nName: {} \nAdmission: {}\nFaculty: {} \nCode: {} \n
    """.format(name, admission, faculty, Coderesent).encode("utf8"))
    
def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("127.0.0.1", 12345))
        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    print('Socket now listening')

    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()
    soc.close()

start_server()  
