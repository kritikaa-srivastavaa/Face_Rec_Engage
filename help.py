from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\hp\Desktop\faceRec\Training_Images\banner.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\hp\Desktop\faceRec\Training_Images\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Help",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        det_img_btn=Image.open(r"C:\Users\hp\Desktop\faceRec\Training_Images\fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\hp\Desktop\faceRec\Training_Images\yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=710,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\hp\Desktop\faceRec\Training_Images\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)


        # create function for button 
    
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()