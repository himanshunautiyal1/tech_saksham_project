import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
st.image("./cc.png")
def connect_db():
    conn=sqlite3.connect("main.db")
    return conn
def create_table():
    conn=connect_db()
    cur=conn.cursor()
    cur.execute("create table if not exists USER (Mail varchar(75),Phone_No integer,Username varchar(20),Password varchar(20),PRIMARY KEY (Mail))")
    conn.commit()
    conn.close()
def create_profile(data):
    conn=connect_db()
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO USER(Mail,Phone_No,Username,Password) VALUES (?,?,?,?)", data)
        conn.commit()
        conn.close()
        return 1
    except slite3.IntegrityError:
        st.error("User already Registered")
        conn.close()
def college():
    conn=connect_db()
    cur=conn.cursor()
    if st.session_state.get("exam")=="JEE Mains":
        if st.session_state.get("ten") >=50 and st.session_state.get("twelve") >=50:
            if st.session_state.get("course")=="B.Tech":
                if st.session_state.get("exam_op"):
                    r=st.session_state.get("exam_score_op")
                    cur.execute("Select* from JEE_AD where Marks < (?)",(r,))
                    c=cur.fetchall()
                    if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                    else:
                        st.subheader("No college found")

                    cur.execute("Select* from JEE_MAINS")
                    c=cur.fetchall()
                    for colleges in c:
                        st.write("*"*50)
                        st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                        st.write("*"*50)
                else:
                    r=st.session_state.get("exam_score")
                    cur.execute("Select* from JEE_MAINS where Marks < (?)",(r,))
                    c=cur.fetchall()
                    if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                    else:
                        st.subheader("No college found")
            else:
                if st.session_state.get("exam_op"):
                    r=st.session_state.get("exam_score_op")
                    cur.execute("Select* from JEE_AD where Marks < (?)",(r,))
                    c=cur.fetchall()
                    if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                    else:
                        st.subheader("No college found")
                    cur.execute("Select* from JEE_MAINS")
                    c=cur.fetchall()
                    for colleges in c:
                        st.write("*"*50)
                        st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                        st.write("*"*50)
                else:
                    r=st.session_state.get("exam_score")
                    cur.execute("Select* from JEE_MAINS where Marks < (?)",(r,))
                    c=cur.fetchall()
                    if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                    else:
                        st.subheader("No college found")
        else:
            st.subheader("No College Found")

    elif st.session_state.get("exam")=="NEET":
        if st.session_state.get("ten") >=50 and st.session_state.get("twelve") >=50:
            if st.session_state.get("course")=="MBBS":
                r=st.session_state.get("exam_score")
                cur.execute("Select* from MEDICAL where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
            else:
                r=st.session_state.get("exam_score")
                cur.execute("Select* from MEDICAL where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
        else:
            st.subheader("No College Found")

    elif st.session_state.get("exam")=="HSEE":
        if st.session_state.get("ten") >=50 and st.session_state.get("twelve") >=50:
            if st.session_state.get("course")=="BA":
                r=st.session_state.get("exam_score")
                cur.execute("Select* from ARTS where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
            else:
                r=st.session_state.get("exam_score")
                cur.execute("Select* from ARTS where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
        else:
            st.subheader("No College Found")

    elif st.session_state.get("exam")=="CUET (Maths)":
        if st.session_state.get("ten") >=50 and st.session_state.get("twelve") >=50:
            if st.session_state.get("course")=="B.Com":
                r=st.session_state.get("exam_score")
                cur.execute("Select* from COMMERCE where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
            else:
                r=st.session_state.get("exam_score")
                cur.execute("Select* from COMMERCE where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
        else:
            st.subheader("No College Found")

    elif st.session_state.get("exam")=="CUET (IP)":
        if st.session_state.get("ten") >=50 and st.session_state.get("twelve") >=50:
            if st.session_state.get("course")=="B.Com":
                r=st.session_state.get("exam_score")
                cur.execute("Select* from COMMERCE where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
            else:
                r=st.session_state.get("exam_score")
                cur.execute("Select* from COMMERCE where Marks < (?)",(r,))
                c=cur.fetchall()
                if c:
                        for colleges in c:
                            st.write("*"*50)
                            st.write(f"<font size='7'><b>{colleges[0]}</b></font><br>Address: {colleges[1]}<br>College Link: <a href='{colleges[2]}'>{colleges[2]}</a><br>", unsafe_allow_html=True)
                            st.write("*"*50)
                else:
                    st.subheader("No college found")
        else:
            st.subheader("No College Found")
        
    
    conn.close()


                
def info():
    stream=["Science (Biology)","Science (Maths)","Commerce (Maths)","Commerce (IP)","Arts"]
    selected=st.selectbox("Enter your stream: ",stream,key="streamselect",index=None,placeholder="Select an option")
    if selected:
        st.session_state["ten"]=st.number_input("Enter your 10th percentage:",min_value=0.0,max_value=100.0,step=0.1)
        st.session_state["twelve"]=st.number_input("Enter your 12th percentage:",min_value=0.0,max_value=100.0,step=0.1)
        if selected=="Science (Biology)":
            st.session_state["exam"]=("NEET")
            st.session_state["exam_score"]=st.number_input("Enter marks in NEET: ",min_value=0,max_value=720,step=1)
            st.session_state["course"]=st.selectbox("Enter your desired course: ",["MBBS","BDS"],key="courseselect",index=None,placeholder="Select an option")
            if st.session_state["exam_score"] and st.session_state["ten"] and st.session_state["twelve"] and st.session_state["course"]:
                if st.button("Search"):
                    st.session_state.slt=True
                    st.rerun()
        elif selected=="Science (Maths)":
            st.session_state["exam"]=("JEE Mains")
            st.session_state["exam_score"]=st.number_input("Enter your percentile in JEE Mains: ",min_value=0.0,max_value=100.0,step=0.1)        
            if "exam_score_op" not in st.session_state:
                st.session_state["exam_score_op"]=0
            exam_score_op=0
            if st.session_state["exam_score"]>=90:
                exam_score_op=st.number_input("Enter your marks in JEE Advanced (optional): ",min_value=0,max_value=300,step=1)
            st.session_state["exam_score_op"]=exam_score_op
            st.session_state["course"]=st.selectbox("Enter your desired course: ",["B.Tech","B.Arch"],key="courseselect",index=None,placeholder="Select an option")
            if st.session_state["exam_score_op"]:
                st.session_state["exam_op"]=("JEE Advanced")
            else:
                st.session_state["exam_op"]=("")
            if st.session_state["exam_score"] and st.session_state["ten"] and st.session_state["twelve"] and st.session_state["course"]:
                if st.button("Search"):
                    st.session_state.slt=True
                    st.rerun()
        elif selected=="Commerce (Maths)":
            st.session_state["exam"]=("CUET (Maths)")
            st.session_state["exam_score"]=st.number_input("Enter your marks in CUET: ",min_value=0,max_value=750,step=1)
            st.session_state["course"]=st.selectbox("Enter your desired course: ",["B.Com","BCA"],key="courseselect",index=None,placeholder="Select an option")
            if st.session_state["exam_score"] and st.session_state["ten"] and st.session_state["twelve"] and st.session_state["course"]:
                if st.button("Search"):
                    st.session_state.slt=True
                    st.rerun()
        elif selected=="Commerce (IP)":
            st.session_state["exam"]=("CUET (IP)")
            st.session_state["exam_score"]=st.number_input("Enter your marks in CUET: ",min_value=0,max_value=750,step=1)
            st.session_state["course"]=st.selectbox("Enter your desired course: ",["B.Com","BBA"],key="courseselect",index=None,placeholder="Select an option")
            if st.session_state["exam_score"] and st.session_state["ten"] and st.session_state["twelve"] and st.session_state["course"]:
                if st.button("Search"):
                    st.session_state.slt=True
                    st.rerun()
        elif selected=="Arts":
            st.session_state["exam"]=("HSEE")
            st.session_state["exam_score"]=st.number_input("Enter your marks in HSEE: ",min_value=0,max_value=750,step=1)
            st.session_state["course"]=st.selectbox("Enter your desired course: ",["BA","BFA"],key="courseselect",index=None,placeholder="Select an option")
            if st.session_state["exam_score"] and st.session_state["ten"] and st.session_state["twelve"] and st.session_state["course"]:
                if st.button("Search"):
                    st.session_state.slt=True
                    st.rerun()
def verify(mail,password):
    conn=connect_db()
    cur=conn.cursor()
    cur.execute("select * from USER where mail=? and password=?",(mail,password))
    result=cur.fetchone()
    if result!=None:
        conn.close()
        return True
    else:
        conn.close()
        return False
def welcome(mail):
    conn=connect_db()
    cur=conn.cursor()
    cur.execute("select username from user where mail=?",(mail,))
    result=cur.fetchone()
    if result:
        st.subheader(f"Welcome {result[0]}")
def sign_up():
    st.subheader("Sign Up")
    mail=st.text_input("Enter your mail: ")
    mail_error=st.empty()
    phone=st.text_input("Enter your mobile number: ")
    phone_error=st.empty()
    username=st.text_input("Enter a username: ")
    password=st.text_input("Enter a password (minimum 6 characters): ",type="password")
    password_error=st.empty()
    repassword=st.text_input("Enter passowrd again: ",type="password")
    repassword_error=st.empty()
    if st.button("Sign Up"):
        a,b,c,d=0,0,0,0
        if '@' in mail and '.com' in mail:
            d=1
        if (phone.isdigit() and len(phone)==10):
            a=1
        if len(password)>=6:
            b=1
        if repassword==password:
            c=1
        if (a==1 and b==1 and c==1 and d==1):
            if create_profile((mail,phone,username,password)):
                st.success("Successfully Signed Up")
                st.subheader("Now Log In")
        elif (a==1 and b==1 and c==0 and d==1):
            repassword_error.error("Password does not match")
        elif (a==0 and b==1 and c==1 and d==1):
            phone_error.error("Invalid Phone Number")
        elif (a==1 and b==0 and d==1):
            password_error.error("Minimum 6 characters reuired")
        elif (a==1 and b==1 and c==1 and d==0):
            mail_error.error("Invalid mail ID")
        elif (a==0 and b==1 and c==0 and d==1):
            phone_error.error("Invalid Phone Number")
            repassword_error.error("Password does not match")
        elif (a==0 and b==0 and d==1):
            phone_error.error("Invalid Phone Number")
            password_error.error("Minimum 6 characters reuired")
        elif (a==0 and b==1 and c==1 and d==0):
            phone_error.error("Invalid Phone Number")
            mail_error.error("Invalid mail ID")
        elif (a==1 and b==0 and d==0):
            password_error.error("Minimum 6 characters reuired")
            mail_error.error("Invalid mail ID")
        elif (a==0 and b==1 and c==1 and d==0):
            repassword_error.error("Password does not match")
            mail_error.error("Invalid mail ID")
        elif (a==1 and b==1 and c==0 and d==0):
            repassword_error.error("Password does not match")
            mail_error.error("Invalid mail ID")
        elif (a==0 and b==0 and d==0):
            phone_error.error("Invalid Phone Number")
            password_error.error("Minimum 6 characters reuired")
            mail_error.error("Invalid mail ID")
        elif (a==0 and b==1 and c==0 and d==0):
            phone_error.error("Invalid Phone Number")
            repassword_error.error("Password does not match")
            mail_error.error("Invalid mail ID")
def log_in():
    st.subheader("Log In")
    mail1=st.text_input("Enter your mail: ",key="loginem123mail" )
    password1=st.text_input("Enter your password: ",type="password")
    bt=st.button("Log In")
    if "sign" not in st.session_state:
        st.session_state.sign=False
    if bt:
        if verify(mail1,password1):
            st.session_state.logged_in=True
            st.session_state.sign=True
            st.session_state.user_mail=mail1
        else:
            st.error("Incorrect Mail or Password")
    if not st.session_state.sign:
        st.subheader("Not a user? Sign Up")
def about():
    st.subheader("College Counselor is an easy-to-use app that helps students find the right colleges based on their marks. Just enter your scores, and the app will show you a list of colleges you can get into. It checks admission cut-offs and other details to give you the best options. The app provides useful information about Colleges. With a simple design, it makes the college search process stress-free.")
def main():
    with st.sidebar:
        opt=option_menu("Menu",["Log In","Sign Up","About"])
    if "logged_in" not in st.session_state:
        st.session_state.logged_in=False 
    if "page" not in st.session_state:
        st.session_state.page="login"
    if "slt" not in st.session_state:
        st.session_state.slt=False
    if opt=="Log In" and st.session_state.page!="login":
        st.session_state.page="login"
    elif opt=="About" and st.session_state.page!="about":
        st.session_state.page="about"
    elif opt=="Sign Up" and st.session_state.page!="signup":
        st.session_state.page="signup"
    if st.session_state.page=="login":
        log_in()
    elif st.session_state.page=="signup":
        sign_up()
    elif st.session_state.page=="about":
        about()
    if st.session_state.logged_in and opt=="Log In":  
        st.success("Logged In")
        welcome(st.session_state.user_mail)
        if not st.session_state.slt:
            info()
        if st.session_state.slt:
            college()
create_table()
main()

