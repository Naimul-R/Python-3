from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from Course import CourseClass

class RMS:
    def __init__(self, root): 
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===Icons===
        # choose resample filter compatible with Pillow versions
        try:
            resample = Image.Resampling.LANCZOS
        except AttributeError:
            resample = Image.ANTIALIAS

        try:
            logo_img = Image.open("Images/logo_p.PNG")
            logo_img = logo_img.resize((40, 40), resample)
            self.logo_photo = ImageTk.PhotoImage(logo_img)
            self.logo_label = Label(self.root, image=self.logo_photo, bg="#033054")
            self.logo_label.place(x=5, y=5)
        except Exception as e:
            print("Could not load logo image:", e)
            self.logo_photo = None

        #===Titles===
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_photo, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)
        #===Menu===
        M_Frame=LabelFrame(self.root,text="Menus",font=("Time new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=70)

        btn_Course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=30)
        btn_Student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=240,y=5,width=200,height=30)
        btn_Result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=460,y=5,width=200,height=30)
        btn_View=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=680,y=5,width=200,height=30)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=30)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=30)

        #===Content_Window===
        try:
            bg = Image.open("Images/bg_2.png")
            bg = bg.resize((850, 350), resample)
            self.bg_photo = ImageTk.PhotoImage(bg)
            self.bg_label = Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=400, y=180, width=850, height=350)
        except Exception as e:
            print("Could not load background image:", e)
            self.bg_photo = None
            self.bg_label = None

        #===Update_Details===
        self.lbl_course = Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=260,height=100)

        self.lbl_student = Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=700,y=530,width=260,height=100)

        self.lbl_result = Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1000,y=530,width=260,height=100)

        #===Footer=== 
        footer=Label(self.root,text="SRMS-Student Result Managment System\nContract us for any technical issue: 019xxxxxxx71",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def new_method(self):
        # Example helper: re-resize background if needed
        if self.bg_photo is None:
            return
        try:
            # keep original PIL image if you need to resize dynamically; placeholder behavior here
            pass
        except Exception:
            pass

if __name__=="__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()