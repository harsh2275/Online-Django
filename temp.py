import smtplib
import os , imghdr
import qrcode
from email.message import EmailMessage

def func(email,lis_code,lis_nam) :
    qr = qrcode.QRCode(
    version=1,
    box_size=15 
    )
    lis=[]
    i=0
    for x in lis_code:
        print (x)
        qr = qrcode.QRCode(
        version=1,
        box_size=15 
        )
        qr.add_data(x)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        #print("--------",lis_nam[i])
        img.save("./QR_Images/"+"QR_"+lis_nam[i]+str(i)+".png","png")
        lis.append("./QR_Images/"+"QR_"+lis_nam[i]+str(i)+".png")
        i+=1


    email_pass = "techfest#vmh855" 
    email_id = "techfest.hyperloops@gmail.com" 

    msg = EmailMessage()
    msg['Subject'] = 'Ticket has been attached hereby' 
    msg['From'] = email_id
    msg['To'] = email
    msg.set_content("Hereby I am attaching your hyperloops ticket")

    for file in lis:
        with open(file,'rb') as m:
            file_data = m.read()
            file_type = imghdr.what(m.name)
            file_name = m.name

        msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename= file_name) 

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_id,email_pass)
        smtp.send_message(msg)

def remove():
    for file in os.listdir('./QR_Images/'): 
        if file.endswith('.png'):
            os.remove(file) 

#func("harsh.agrawal2274@gmail.com",["kkkk","llll","nnnn"],["harsh","tan","man"])