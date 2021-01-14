import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient('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')

from_email = Email("sahibdeep.singh@financepeer.co")
to_email = To("maliksanjeet88@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "Hi Sanjeet, what's the Plan of Action today?")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)