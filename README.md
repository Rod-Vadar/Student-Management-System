# Introduction

The purpose of this project is to demonstrate the implementation of CRUD using Django.  The website consists of a simple interface for a Student Record management system.
A new student can be created and added to the database, the record can be updated or deleted.  The records are displayed visually on the main admin interface with action buttons.

## User Experience - UX
I designed the interface to be instantly accesible and intuitive for the user experience. I use Font Awesome Icons for user actions which are recognisable.  The icons instantly convery the meaning of the action.  I use a Trashcan for the 'Delete' action and the user immediately undesrtands what this does without requiring any further training.

I feel this is a very important feature for the user experience and ensures the user experience is consistent with the user experience from other well known popular websites.

## Agile
I used www.trello.com to implement the agile approach.

## Epics and User Stories

#### Specimen Users
![Zephyr Design](./user%20images/user-persona1.png)

![Zephyr Design](./user%20images/user-persona2.png)

#### Epic 1 The UI
* Convey the purpose of this project to the user on the landing page / main admin interface
* Provide a simple interface which is intuitive to the user

#### User Relevance
* As a user I want the admin interface to be simple to use.  I want the action buttons to be visible.
* I want to be able to easily add a new record when a new student joins the college.
* I want to be able to update or change the details on the record about the student.
* I want to be able to delete the record when a student leaves the college.

## Tasks
For this project I imagined a website with a simple interface on the landing page which college admin staff could access and add and change student records easily.

I created a simple wireframe using Balsamiq
I created the project in github and started it with codepsaces.
I set up the templates.
I used a css template from Bootswatch (zephyr) to style the site using bootstrap.

##  Design CSS Style
The style of the site comes from https://bootswatch.com/zephyr/

![Zephyr Design](./user%20images/design.png)

## Wireframe

![Wireframe](./user%20images/student_wire.png)

## Actual Design

![actual Design](./user%20images/actual_design_1.png)

![actual Design](./user%20images/actual_design_2.png)

## Functionality

The administrator is responsible for creating a new student record.  They can do this by clicking + Add student.  All details are able to be entered on a single page.

They can also change or update the record by clicking the "Update" icon and they can delete the record simply by clicking the trash icon next to the record.

The design is fully responsive because I used bootstrap with Bootswatch.  On a very small mobile device the icons are not immediately apparent however there is horizontal scrolling capability which makes it possible to access all the record and buttons by finger swiping on the screen.

## Technologies used
Github: https://github.com/
Codespaces from github with VSCode.
Balsamiq Cloud: https://balsamiq.cloud/s84davo/poql9mj/rE39C
HTML5
CSS: Bootswatch: Zephyr Theme and fonts.
JavaScript to load boostrap from the content delivery network.
Python3
Django: Version 3 as Version 4 caused problems which I was not able to resolve.
Bootstrap: Version 5
FontAwesome Icons: For the Action Features.
Google Lighthouse: For performance checking although the site is not actually deployed properly yet.

## Validation
HTML using WC3: I submitted my html files to wc3 but it kept complaining about Django things like {% load static %}
CSS Using WC3: I submitted my CSS file which is an actual theme from Bootswatch.  The validator complained that there are 15 errors in the theme however I am not able to change the theme.
Python using CI Python Linter: I submitted my Python code and no errors are found except for some lines being too long.

## Bugs
Originally I tried to use the latest version of Django 4 for this project. This caused an unresolvable error with a security token and despite extensive searching on Google I was not able to find any solution to this.
I eventually resolved it by removing Django 4 and installing version 3.


## Future upgrades

I would like to add a username and password for the admin to log in.  I would also like to add the campablity for a photo of the student to be uploaded to the record.

I would also like to deploy it to a service such as Heroku.








