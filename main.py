from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import ImageDetection as ImgDetect
import VideoDetection as VdDetection
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


def send():
        sendEmail(TxtEmailFrom.get(),TxtEmailTo.get(), TxtSubject.get(), TxtDescription.get("1.0", 'end-1c'))


def browseImage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image Flle",
                                     filetypes=(("JPG File", "*.jpg"), ("JPG File", "*.jpg"), ("PNG file", ".png"),
                                                ("All Files", "*.*")))
    ImgDetect.detectImage(fln)
    LabelResultat = Label(window, textvariable=fln, text=fln, fg='white' ,background='black')
    LabelResultat.place(x=500, y=300)
    image1 = Image.open('ImgToSend/img0.jpg')
    image1 = image1.resize((400, 280), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    # Position image
    label1.place(x=400, y=10)

def startVideo():
    VdDetection.detectVideo()

def sendEmail(emailFr,emailTo,subject,description):
    message = Mail(
        from_email=emailFr,
        to_emails=emailTo,
        subject=subject,
        html_content=description)
    with open('ImgToSend/img0.jpg', 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('img0.jpg'),
        FileType('application/image'),
        Disposition('attachment')
    )
    message.attachment = attachedFile
    sg = SendGridAPIClient('api_key')
    sg.send(message)

window = Tk()
window.geometry("850x350")
window.title('Object detection')
window.iconbitmap('logo.ico')
window.config(background='black')
lblE1 = Label(window, text="détection d'objet",font=('Calibri', 18),fg='white' ,background='black')
lblE1.place(x=150,y=10)
lblEMailFrom = Label(window, text='Email address',fg='white' ,background='black')
lblEMailFrom.place(x=50,y=50)
TxtEmailFrom = Entry(window)
TxtEmailFrom.place(x=150,y=50, width=170 ,height=20)
lblEMailTo = Label(window, text='Email address To',fg='white' ,background='black')
lblEMailTo.place(x=50,y=100)
TxtEmailTo = Entry(window)
TxtEmailTo.place(x=150,y=100, width=170 ,height=20)
lblSubject = Label(window, text='Subject',fg='white' ,background='black')
lblSubject.place(x=50,y=150)
TxtSubject = Entry(window)
TxtSubject.place(x=150,y=150, width=170 ,height=20)
lblDescription = Label(window, text='Content',fg='white' ,background='black')
lblDescription.place(x=50,y=200)
TxtDescription = Text(window)
TxtDescription.place(x=150,y=200, width=230 ,height=70)
btnSend = Button(window, text='Send', command=send)
btnSend.place(x=70,y=300)
btnVideo = Button(window, text='Start video', command=startVideo)
btnVideo.place(x=150,y=300)
lbl = Label(window)
lbl.place(x=400,y=50)
buttonExit = Button(window, text="Exit" ,command=lambda: exit())
buttonExit.place(x=250,y=300)
button5 = Button(window, text="Browse Image" ,command=browseImage)
button5.place(x=400, y=300)

image0 = Image.open('images/img4.jpg')
image0 = image0.resize((400, 280), Image.ANTIALIAS)
test0 = ImageTk.PhotoImage(image0)

label1 = Label(image=test0)
label1.image = test0
# Position image
label1.place(x=400, y=10)

window.mainloop()