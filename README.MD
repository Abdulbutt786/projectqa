# QA-finalproject

## Movie Review Website

This contains a flask based CRUD application that I built. This is my first project.
### Table of contents

[Project introduction](#Project-introduction)

[Designing the application](#Designing-the-application)

[Project tracking](#Project-tracking)

[Risk assesment](#Risk-assesment)

[Testing phase](#Testing-phase)

[The application](#The-application)

[CICD Pipeline](#CICD-Pipeline)

[Known app issues](#Known-app-issues)

[Challenges faced](#Challenges-faced)

[Possible future changes to application](#Possible-future-changes-to-application)

[Conclusion and learning from this project](#Conclusion-and-learning-from-this-project)

[Credits](#Credits)

### Project introduction

This project was a very intense project and was a way of testing our knowledge of all the weeks off learing. The application that we were told to create had to apply CRUD (Create, Read, Update and Delete). In addition, it must contain  database that is able to link with MYSQL and have a one to many relationship at the very least. 

### Designing the application

I decided to create movie review site as it would enable me to satisfy all the functions of a CRUD appliation. I decided to make a one to many application. The idea was that a user can create an account on my website and they are able to go to the reviews page in which they can update and delete their reviews. 
The below ERD (Entity Relationship Diagram) will shows my relationships between the models:

<img width="688" alt="Screenshot 2022-06-16 at 20 07 35" src="https://user-images.githubusercontent.com/104978376/174146713-d2a0c86a-7f70-47fd-9326-c5ba3ed58b16.png">

This ERD diplays a one to many relationship between the models User and Review. A single user can create multiple reviews - whilst on the other hand a review can only be linked to one user. 

### Project tracking 
I used the Jira application to keep track off my progress this help me with managing my team and ensuring I know what is needed to complete the application. I have put the main function as should have within the trello board as these are the essentials in order to complete my CRUD app. 

This is my jira board below:

<img width="1408" alt="Screenshot 2022-06-16 at 20 57 46" src="https://user-images.githubusercontent.com/104978376/174153841-68a28c3e-3f14-42f2-928c-3fb4c6502471.png">




### Risk Assesment

I have created a risk which would highlight the risks I would face when creating the application and how I would action a solution in order to resolve them. These will help me from mitigating the threats to my application to better the security in order to get it deployed as quickly and safely as possible with no bugs. 

This is my risk assesment below:


<img width="489" alt="Screenshot 2022-06-16 at 22 02 59" src="https://user-images.githubusercontent.com/104978376/174163193-e15148a1-ce35-4a23-b1da-f846fa3d2d11.png">



### Testing phase
This was a vital stage off my application. This allows me check the validity of the codes I have written in my application. This was done in an orderly manner first I made sure that all functions were functioning correctly and then I checked that the routes were providing the correct response. 

I achieved 96% coverage and once I achieved this I movied on to jenkins as part of my CI/CD pipeline.
In addition to this I used webhooks on Jenkins and everytime I ran a new build Jenkins would automatically make any changes to my code and run the unit tests. 

I have attached the pictures below off my tests:

<img width="903" alt="Screenshot 2022-06-16 at 22 04 59" src="https://user-images.githubusercontent.com/104978376/174163420-65e7189b-4d9e-42d9-8ae9-33e5fe8f363e.png">

Due to time contraints and the time remaining I had to complete the rest of the coverage I was unable to achieve 100%. But I was very proud I was able to achieve 96% on my first ever project. In addition to this with more learning I will be able to tackle how to tackle the last 4%.

The picture below will show my coverage in a html file. This coverage is after I have deployed my application with jenkins. 

https://github.com/Abdulbutt786/projectqa/blob/20d660703527258682d782a3cfe84d98307ecdd9/application/Photos/Screenshot%202022-06-17%20at%2010.40.37.png


### The application
This is brief overview off my application how it works, showing you different pages and functions it provides users with. 

Home Page
The home page is black and the nav bar has a button for users to create an account.

Home Page
<img width="811" alt="Screenshot 2022-06-16 at 22 06 15" src="https://user-images.githubusercontent.com/104978376/174163780-f562d884-2eed-4bc9-9734-971d8a53b123.png">



Create User 
Once users clicked create user in the nav-bar, they are taking to this form they have to fill out. 
<img width="1391" alt="Screenshot 2022-06-16 at 22 06 54" src="https://user-images.githubusercontent.com/104978376/174163804-723e2224-c783-4b68-b4e2-301b06402a82.png">

Once users have created an account they are taken to this page where they have two options which is to create a review or view all their reviews which satisfies to off the CRUD functionailities.

<img width="1340" alt="Screenshot 2022-06-16 at 22 07 01" src="https://user-images.githubusercontent.com/104978376/174164296-93fb3fe9-2fa4-4c65-8f26-83c0ad77ba1f.png">


 Review Form                
 The review form is the link between the User and Reviews - this is where the relationship is established. One user can have many reviews (One to many)
 
 <img width="1352" alt="Screenshot 2022-06-16 at 22 09 48" src="https://user-images.githubusercontent.com/104978376/174164163-1e16fbbe-0b18-4098-b0e0-0126f9cc8123.png">
                                                       
                                                               
Review Submitted -  This takes them back to a page where they can see the Update buttom to change their review and the delete button if they have changed their mind. 


<img width="1418" alt="Screenshot 2022-06-16 at 22 07 23" src="https://user-images.githubusercontent.com/104978376/174164097-19d62347-b526-427f-9c97-21d0dd2bba35.png">


### CICD Pipeline


### Known application issues


### Challenges faced



















form not showing mobile phoone number for user

when users create account redirect to home page where it shows all users

when they create a new user redirect to homepage

creating buttons so it takes users to their reviews and to create a new one 
