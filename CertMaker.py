from PIL import ImageFont, ImageTk, ImageDraw, Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter
from tkinter import messagebox, filedialog
from tkinter.colorchooser import askcolor
import os
from PIL.Image import Resampling


def send_emails(filename, toaddr):
    fromaddr = "EMAIL"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = txt1.get("1.0", "end-1c") if not None else ""

    # string to store the body of the mail
    body = txt2.get("1.0", "end-1c") if not None else ""

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    # filename = "cert.png"
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "PASSWORD") # In here, if using gmail, you'd have to use the app password

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

def make_lists(filename):
    file = open(filename, "r")
    lines = file.readlines()
    names = []
    emails = []
    for line in lines:
        name, email = line.strip("\n").split(",")
        names.append(name)
        emails.append(email)

    return names, emails


def main():
    messagebox.showinfo("Starting", "Starting")

    names, emails = make_lists(csv_filename.get())
    for i in range(len(names)):

        # Open an Image
        img = Image.open(png_filename.get())
        W = img.width

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype(ttf_filename.get(), int(v2.get()))
        left, upper, right, lower = myFont.getbbox(names[i])
        wid = right-left
        #h = upper-lower
        #wid, h = myFont.getsize(names[i])
        #draw.text(((W - w) / 2, (H - h) / 2), msg, font=arial, fill="black")

        # Add Text to an image
        I1.text(((W - wid) / 2, int(v1.get()) if not None else 430), names[i], font=myFont, fill=color.get())

        # Display edited image
        #img.show()

        # Save the edited image
        if not os.path.exists('Images'):
            os.mkdir('Images')
        filename = f"Images/{names[i]}.pdf"
        im1 = img.convert('RGB')
        im1.save(filename)
        email = emails[i]

        send_emails(filename, email)
    messagebox.showinfo("Ended", "Ended")


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    if "csv" in filename:
        csv_filename.set(filename)
    elif "png" in filename:
        png_filename.set(filename)
        # img = Image.open(png_filename.get())
        # height.set(img.height)
    elif "ttf" in filename or "otf" in filename:
        ttf_filename.set(filename)

# def print_it():
#     print("csv:", csv_filename.get())
#     print("png:",png_filename.get())
#     print("ttf:",ttf_filename.get())

def prev_img():
    # Open an Image
    img = Image.open(png_filename.get())
    W = img.width

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(ttf_filename.get(), int(v2.get()) if not None else 180)
    # wid, h = myFont.getsize(v3.get())
    # draw.text(((W - w) / 2, (H - h) / 2), msg, font=arial, fill="black")
    left, upper, right, lower = myFont.getbbox(v3.get())
    wid = right - left

    # Add Text to an image
    I1.text(((W - wid) / 2, int(v1.get())), v3.get(), font=myFont, fill=color.get())
    img.show()


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    color.set(colors[1])


window = tkinter.Tk()

window.title("Script Sender")

csv_filename = tkinter.StringVar(window, value="")
png_filename = tkinter.StringVar(window, value="")
ttf_filename = tkinter.StringVar(window, value="")
color = tkinter.StringVar(window, value="#0889C3")




lbl = tkinter.Label(window, text="Import csv with names and emails")
lbl.pack(anchor="center")
btn = tkinter.Button(window, text="Upload .csv", command=UploadAction)
btn.pack(anchor='center')
lbl2 = tkinter.Label(window, text="Import png certificate template")
lbl2.pack(anchor="center")
btn2 = tkinter.Button(window, text="Upload .png", command=UploadAction)
btn2.pack(anchor='center')
lbl4 = tkinter.Label(window, text="Import font")
lbl4.pack(anchor="center")
btn4 = tkinter.Button(window, text="Upload .ttf", command=UploadAction)
btn4.pack(anchor='center')
lblclr = tkinter.Label(window, text="Color picker")
lblclr.pack(anchor="center")
btnclr = tkinter.Button(window, text="Choose Color", command=change_color)
btnclr.pack(anchor="center")
lbl8 = tkinter.Label(window, text="Test String")
lbl8.pack(anchor="center")
v3 = tkinter.Entry(window, justify="center")
v3.pack(anchor="center")
v3.insert(0,"Lorem Ipsum")
lbl3 = tkinter.Label(window, text="Set height")
lbl3.pack(anchor="center")
# v1 = tkinter.IntVar()
# w1 = tkinter.Scale(window, from_=0, to=2000,variable=v1, orient="horizontal")
# w1.pack(anchor="center")
v1 = tkinter.Entry(window, justify="center")
v1.pack(anchor="center")
v1.insert(0,"500")
lbl5 = tkinter.Label(window, text="Set Font Size")
lbl5.pack(anchor="center")
v2 = tkinter.Entry(window, justify="center")
v2.pack(anchor="center")
v2.insert(0,"180")
# v2 = tkinter.IntVar()
# w2 = tkinter.Scale(window, from_=0, to=300, variable=v2,orient="horizontal")
# w2.pack(anchor="center")
btn5 = tkinter.Button(window, text="Preview Image", command=prev_img)
btn5.pack(anchor='center')
lbl6 = tkinter.Label(window, text="Enter Email Subject: ")
lbl6.pack(anchor='center')
txt1 = tkinter.Text(window, height=5, width=25, bg = "light cyan", fg="black")
txt1.pack(anchor='center')
lbl7 = tkinter.Label(window, text="Enter Email Body: ")
lbl7.pack(anchor='center')
txt2 = tkinter.Text(window, height=5, width=25, bg = "light cyan", fg="black")
txt2.pack(anchor='center')
btn6 = tkinter.Button(window, text="Run Script", command=main)
btn6.pack(anchor='center')
window.mainloop()
