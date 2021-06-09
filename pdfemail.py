import smtplib
import imghdr
from email.message import EmailMessage
from fpdf import FPDF

def pdf_mail(msg,cont):
    pdf = FPDF()
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(200, 20, txt = "Covac Vaccination Portal", 
         ln = 1, align = 'J')
    pdf.set_font("Arial", size = 15)
    c=2
    for i in msg:
      s = i+' : '+str(msg[i])
      pdf.cell(20, 10, txt = s, 
         ln = c, align = 'J')
      c+=1

    pdf.output("covac.pdf") 

# email
    Sender_Email = "tnvaccinationportal@gmail.com"
    Reciever_Email = "nandhabalanmarimuthu15@gmail.com"
    Password = 'vaccine123'

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Vaccination Portal" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content(cont) 

    files = ['covac.pdf']

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
