import imaplib
import email
from email.header import decode_header

imap_url = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(imap_url)
mail.login("test", "test_pass")
gmail_host= 'imap.gmail.com'
#select inbox
mail.select("INBOX")

#select specific mails
frase = "writing you this email from Hawaii."
_, selected_mails = mail.search(None, '(BODY "urlreq:")')

#total number of mails from specific user
print("Total Messages:" , len(selected_mails[0].split()))

for num in selected_mails[0].split():
    _, data = mail.fetch(num , '(RFC822)')
    _, bytes_data = data[0]

    #convert the byte data to message
    email_message = email.message_from_bytes(bytes_data)
    print("\n===========================================")

    #access data
    assunto = email_message["subject"]
    decoded_subject, encoding = decode_header(assunto)[0]
    if isinstance(decoded_subject, bytes):
        decoded_subject = decoded_subject.decode(encoding or 'utf-8')
        print("Subject: ",decoded_subject)
    print("To:", email_message["to"])
    print("From: ",email_message["from"])
    print("Date: ",email_message["date"])
    for part in email_message.walk():
        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
            message = part.get_payload(decode=True)
            print("Message: \n", message.decode())
            url = message.split()[1].decode('utf-8')
            print("==========================================\n")
            break
