
def send_email(name,email,height,average_height,count_height):
    import smtplib
    from string import Template#allows for subtitution
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage

    
    
    
    def template_reader(filename):
        with open(filename,'r',encoding='utf-8') as file:
            draft=file.read()
            return Template(draft)
        
        
    template_content=template_reader("nice.txt")
    password="nanabaasika06"
    from_email="boazmicah2@gmail.com"
    to_email=email
    subject="Height data"
    gmail=smtplib.SMTP(host="smtp.gmail.com",port=587)
    gmail.starttls()
    gmail.login(from_email,password)
    msg=MIMEMultipart()
    message=template_content.substitute(PERSON_NAME=name,HEIGHT=height,PEOPLE=count_height,AVERAGE_HEIGHT=average_height)
    with open("height_love.jpeg", 'rb') as fp:
        img = MIMEImage(fp.read())
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    msg.attach(MIMEText(message,'plain'))
    
    img.add_header('Content-ID', '<{}>'.format("height_love.jpeg"))
    msg.attach(img)
    gmail.send_message(msg,img.as_string())
    gmail.quit()

#send_email("Boaz","boazmicah2@gmail.com","250","200","50")






















        
