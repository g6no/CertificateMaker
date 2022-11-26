# CertificateMaker
A python certificate maker that automatically overlays names and sends them to the appropriate emails

<img width="207" alt="Tk Sample" src="https://user-images.githubusercontent.com/57629248/204089222-aea7547d-1f56-4b53-b41a-ab6545edae63.png">

It takes the following as parameters:
  - A csv file with names and emails
  - A png template to be for names to be overlaid
  - The font file to be used
  
 It can then be customized by:
  - Choosing the color for the text
  - Choosing the location (height) of the text
  - Setting the appropraite font size for the text
  - Adding an email subject
  - Adding an email body
  
The script will automatically create a pdf certificate for each name on the csv file, and sends them to the appropraite email


Notes:
  - The text is automatically centered
  - Doesn't work with Arabic names
  - For authentication, you'd have to use the gmail app password, more can be found in: https://support.google.com/accounts/answer/185833?hl=en
