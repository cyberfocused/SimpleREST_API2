# 

## Step #1 -once I have set up all of the folders in Visual Studio Code, I open a new terminal window
##          and type npm initialize (node package manger- this creates the "package.json" file)
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/1.jpg) 

## Step #2 -in the terminal window I type "npm install express" 
##          then "Set-ExecutionPolicy unresticted"
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/2.jpg) 

## Step #3 - the app on line 3 I have entered into code will handle the API requests
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/3.jpg) 

## Step #4 - Here I am testing the API code I have so far
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/4.jpg) 

## Step #5 - I tested to see that the http mesage loads in a browser:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/5.jpg) 

## Step #6 -I added app.get, app.post, app.put, and app.delete in my code and then tested each function in Postman:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/6.jpg) 

## Step #7 -testing the Get function in Postman:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/7.jpg) 


## Step #8 -testing the Post function in Postman:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/8a.jpg) 

## Step #9 -testing the Put function in Postman:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/9a.jpg) 

## Step #10 -testing the Delete function in Postman:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/10a.jpg) 

## Step #11 -I added two new patients and records for each of them:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/11.jpg) 

## Step #12 -When I send the request to the API, I want to be able to
## validate the person to make sure they exist ( that their SSN# matches
## and that the appropriate record is returned. The header of the 
## HTTP request is used to send the authentication data
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/12.jpg) 

## Step #13 -I request the medical records in the body:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/13b1.jpg) 

## ... the medical records request printed in the Terminal:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/13b2.jpg)

## Step #14 -I request the medical records in the body:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/14.jpg)

## Step #15 -I entered code for VS Code to generate a "Status Code 404 error#
## if the wrong SSN# is entered:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/15c.jpg) 

## ... I enter an INVALID SSN# in Postman to test:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/15a.jpg)

## ...  Postman generates Status Code- '404 Not Found :
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/15d.jpg)

## Step #16 -Code created in Visual Studio that will generate errors if
## if the first and lat names are correct but ssn# is incorrectly entered:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/16a.jpg) 

## ... error "401 Unauthorized is generated "first/Last name didn't match SSN":
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/16b.jpg)

## Step #17 - if the patient requests his records they will dislay:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/17.jpg) 

## ... error "501 will display if the records are improperly requested":
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/17a.jpg)

## Step #18 - creating a new patient in Postman:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/18a.jpg) 

## ... code for the new patient and it prints in the terminal:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/18b.jpg)

## Step #19 - Using the Put method: I update existing Patient phone number:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/19a.jpg) 

## ... error - Patient not found:
![image](https://github.com/cyberfocused/SimpleRest_API2/blob/main/19b.jpg)
