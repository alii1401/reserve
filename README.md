# Appointment reservation
This site is for online booking of doctor's appointment, where the user can easily register her appointment.
### Site Features
#### 1) Daily Schedule:
Using this feature, you can see the schedule of doctors in the coming days, weeks and months.

**Its function is as follows:** by entering the desired date in the specified format in the form input and pressing the search button, the doctor's schedule will be displayed.
It should be noted that if the entered date is for the current day or earlier, the system will inform the user of this issue with an error message.
Also, if there is no medicine in the entered date, the system will give an error message.

**The result** is displayed in a table that includes information such as specialty, doctor's name, admission capacity, remaining capacity, date and time of visiting the hospital or office.

#### 2) Reserve:
Using this feature, you can register your appointment with the desired doctor at a specific time and date.

**Its function is as follows:** The reservation form has four fields: name, contact number, appointment registration date and desired doctor.
If the national code and the contact number are less than or more than the minimum and maximum, the system will give an error message. If even one field is empty, the user will be faced with a warning message again. Also, if the entered date has passed or there is a current blur or there is no medicine on that date, the user will get an error message.
Finally, if everything is the same, if there is an empty capacity, the turn will be registered for the user.

#### 3) My Appointment: 
By using this feature, the user can make sure whether the turn has been successfully registered for him or not.
In case of successful registration, he can view his appointment information.
Otherwise, the system will print the message that the turn is empty.

#### 4) Adding doctor with using django admin:
Because the person who adds the list of doctors owns the site, so any changes or additions are done using Django Admin.

### Distinguishing this project from other previous projects:

#### 1) Google(search):
This fianl project does not have any functionality in front of the contents that the user intends to search on Google.

#### 2) Wiki:
This fianl project does not provide important and scientific content for users to use or add.

#### 3) Commerce:
In this fianl project, products are not put up for auction on the site so that users can buy.

#### 4) Email:
This fianl project is not designed for social messaging.

#### 5) Network:
In this fianl project, users cannot share their texts on their personal page for others to see and like.

### Files in the project

**layout.html:**   This file contains the main structure of the HTML files of the project, and in other words, the HTML files inherit from this.
**index.html:**    This file includes reservation form, scheduling form and separators used in JavaScript to add text or table.
**login.html:**    This file used for user login.
**register.html:** This file used for user register.
**front-end.js:**  In this file, the front site codes are written.
**styles.css:**    This file was to beautify the site, but since linking from HTML to CSS did not work, styling was done in HTML files.
**serializers.py:**This file is for serializing the objects of the models in the form of Jason so that we can send them to the front.
**views.py:**      This file contains the back and site codes for sending and receiving requests from the client side to the server or vice versa.
**urls.py:**       This file is for writing the paths that we are going to use to communicate with the respective views in each path in the front or back.
**db.sqlite3:**    This file used for save database.

### Run project
I don't need to provide you with additional information to implement the project.

###### *Hoping for success in the final project and receiving a degree in web programming with Python and JavaScript from Harvard University*
###### *Ali Abdollahi, Student of University of Tehran*
