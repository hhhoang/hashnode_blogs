## Automate your Outlook email with Python

We have some tasks that we would like to automate. For example, you want to automate sending email to a certain audience with a written template and attach some files. Or you want to retrieve emails received from a particular sender and save the attachments. 

Your hero package is here to help: win32com. If you use Python through Anaconda, then win32com is already included. You just need to import it. If not you can install the package using pip as follow:

```
pip install pywin32
``` 

At first, let's import some packages and create a Class named OutlookAutomation and with established connection to outlook.

```
import win32com.client as win32
from datetime import datetime
import os

class OutlookAutomation():
    def __init__(self):
        self.outlook = win32.Dispatch('outlook.application')
``` 



**1. Sending a scheduled email with attachment**

Then we create a function sendEmail where we create an empty email, start adding the title of the email, the recipient as well as the copied recipients, we write content in form of HTML, attach the attachment and hit the send button.
```
    def sendEmail(self, subject, main_recipient, cc_repicients, content, attachment_filename):
        try:
            # create an empty email
            mail = self.outlook.CreateItem(0)
            
            # set the email subject
            mail.Subject = subject
            
            # set the recipient email
            mail.To = main_recipient
            mail.cc = cc_repicients
                       
            # Email content
            mail.HTMLBody = content
    
            # add the pdf attachment
            mail.Attachments.Add(os.getcwd() + "\\" + attachment_filename)
            mail.Send()
            print('Finish sending email.')
        except Exception as e:
             print(str(e) + " an error occurs")
``` 
After that we can instantiate a OutlookAutomation and call the function sendEmail with required input.


```
# create an instant of outlookautomation
automateOutlook = OutlookAutomation()

# input for function sendEmail

subject = 'Sales Performance for ' + datetime.now().strftime('%b %Y')
main_recipient = "jane.doe@gmail.com"
cc_repicients = "jane.doe.2@gmail.com; jane.doe.3@gmail.com"
content = r"""
        
        Dear all,<br><br>
        <br><br>
        please find attached the Sale Dashboard.
        <br><br>
        Link
        <br><br>
        For details please contact our XYZ department.
        <br><br>
        Regards,<br><br>
        ABC
        """
attachment_filename ='dashboard.pdf'

# call function sendEmail
automateOutlook.sendEmail(subject, main_recipient, cc_repicients, content, attachment_filename)    

``` 


**2. Read email from a particular sender and save attachment **

Imagine our partner sends us a report every month and we have to read the email and save some files for further analysis, we want our program to search for that particular email and save that file in a particular folder in just one click. 

```
    def retrieveEmail(self, outlook_email, required_sender_email, processed_subfolder,  a_type, file_destination):
        # you have to overwrite your outlook with GetNamespace MAPI in order to retrieve info in the inbox
        self.outlook = self.outlook.GetNamespace("MAPI")
        inbox = self.outlook.Folders[outlook_email].Folders["Inbox"]
        messages = inbox.Items
        for msg in list(messages):
            try:
                if (msg.Sender.GetExchangeUser().PrimarySmtpAddress == required_sender_email):
                    for attachment in msg.Attachments:
                        # only retrieve those with attachment in a certain format
                        if str.lower(attachment.FileName[-3:]) == a_type:
                            temp_filename = os.path.join(file_destination, attachment.FileName)
                            attachment.SaveAsFile(temp_filename)
                            # the subfolder should exist one level after Inbox
                            # otherwise you have to keep writing .Folders['A'].Folders['B']...
                            msg.Move(inbox.Folders[processed_subfolder])
            except Exception as e:
                pass                     
``` 

After that we can call the function and pass in our parameters. 


```
outlook_email = "jane.doe@gmail.com"
required_sender_email = 'john.doe@outlook.com'
processed_subfolder = 'processed'
file_destination = r'C:\Users\Desktop'
automateOutlook.retrieveEmail(outlook_email, required_sender_email, processed_subfolder, 'pdf', file_destination)
``` 
Et voila. Please play around and let me know if it works. For further information about outlook and so on, you can refer [to this document](https://docs.microsoft.com/en-us/office/vba/api/overview/outlook). Eventhough it is in VBA but there are alot of information and similarities that can be refered to.

Happy coding!

