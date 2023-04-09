from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

@app.route('/input-form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        issue_type = request.form['issue_type']
        issue_description = request.form['issue_description']
        ticket_id = create_ticket(name, email, issue_type, issue_description)
        send_email(name, email, ticket_id)
        return redirect('/thank-you')
    return render_template('input-form.html')

if __name__ == '__main__':
    app.run()
