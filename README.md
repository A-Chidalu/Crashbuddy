# Crashbuddy

## Description
An Text Messaging Application for Road Side Assistance (Created at Hackthe6 08/23/2019)

A User Sends an MMS to their specific Twilio account number. Through HTTPS calls and Flask the image is downloaded locally to a directory
in my compter. 

With the directory we then feed this image into a Trained Machine learning Model Made with IBM watson and IBM watson is able to identify and Label
what kind of accident this was. It has 9 Different labels such as(Minor Dent, Minor Scratch, No damage, Car Completley Destoryed, etc...).

Through IBM watson's APIS we are able to retrieve the JSON file of the API call and extract the relavant information from it.

We then are able to send the label back to our user with a score of how confident the IBM watson model was (A percentage).

## Technologies Used
Twilio,Flask,ngrok,Python,IBM WATSON Visual Recogniotion Software, APIS

![CrashbuddyDemo](https://github.com/A-Chidalu/Crashbuddy/blob/master/CrashBuddy%20Demo.jpg?raw=true)
