def create_ticket(name, email, issue_type, issue_description):
    # code to create ticket and store it in the database
    ticket_id = generate_ticket_id() # generate unique ticket id
    # code to store ticket details in the database
    return ticket_id

def send_email(name, email, ticket_id):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your-email@gmail.com" # replace with your email address
    password = "your-password" # replace with your password
    receiver_email = email
    message = f"""Subject: Ticket Confirmation\n\nDear {name},\n\nThank you for submitting your ticket. Your ticket has been received and is being processed. Your ticket ID is {ticket_id}. We will get back to you shortly.\n\nBest Regards,\nThe Support Team"""
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
