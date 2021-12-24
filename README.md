# MicroManage-A-Microbusiness-Manager-Program
Software Design Laboratory (LBYCPD2) course using the Python programming language for the postgreSQL database, the HTML and the CSS structural languages in the PyCharm software.

**Version 1.8**

A microbusiness manager program that allows for the record keeping of data in managing transactions created, the products and raw materials used within the business, as well as the analysis of the trends of the business' income, including its item trends.

## Description

The project MicroManage, which is a microbusiness manager program, generally acts as a business management tool for small businesses that allow for the record keeping of data in terms of its capability in tracking transactions and profit analysis. The program will allow its users to create unique and secure accounts to store and organize the relevant information of their business, such as the maintaining databases on transacted orders, products that the user is selling, as well as the raw materials necessary for each of these products. Additionally, the program also allows for the presentation and analysis of data regarding the demand on specific products, its raw material costing per product, and the trends in the items purchased over a set period of time.

## Getting Started

### Requirements and Dependencies
<ul>
  <li>Windows 10</li>
  <li>PyCharm Professional ver. 2020.3.4</li>
  <li>Python ver. 3.8</li>
  <li>PostgreSQL ver. 13.0</li>
  <li>pgAdmin ver. 5.0</li>
  <li>Bootstrap ver. 4.0</li>
  <li>Chart.js</li>
  <li>Django-crispy-forms</li>
</ul>

### Installing the Program

The program may directly be downloaded from the given GitHub Repository. On the contrary, a complete documentation of the iteration of the program may be found within the Google Drive linked <a href="https://drive.google.com/drive/folders/1-Cq-PJED2ZSbCDUUvhU7sbSt85TM4_Wq">here</a>. The files must be viewed as <i>last modified</i> to find the most recent iteration.

Once the file has been installed, extracted, and opened in PyCharm, an interpreter must then be set up by modifying the <i>Edit Configurations</i> tab of the project, specifically the <b>.exe</b> file available under the downloaded Python version of the interpreter. 

### Executing the Program
<b>Within the Python Terminal of Pycharm:</b>
<ol>
  <li>Execute the command <b>pip install django-crispy-forms</b></li>
  <li>Execute the command <b>py manage.py runserver</b></li>
  <li>Click the provided URL within the Python Terminal</li>
  <ol type='a'>
    <li><b>IF page is still not found</b>, append <b>login</b> at the end of the URL.</li>
  </ol>
  <li>Login Page will be displayed.</li>
  <li>User may view an <i>About Us</i> and <i>Contact us</i> page.</li>
  <ol type='a'>
    <li>Login Credentials will be asked if there is an existing account.</li>
    <li>User may opt to register to create an account.</li>
    <ol type='i'>
      <li>Upon registration of username and password, the business' products and raw materials are requested.</li>
    </ol>
  </ol>
  <li>Home Page will be displayed.</li>
  <li>The summarized content of the business will be displayed, showing the gross and net income of the business, the most sold item, and graphical representation of the data retrieved within the accumulated databases. As of the moment, only the most sold product of the business is shown at the home page.
  <li>User may opt to execute the following pages</li>
    <ol>
      <li><i>Add New Order</i> to add a new transaction to be added to the database</li>
      <li><i>Add Product</i> to add a new product that may be chosen in adding an order/transaction to the database</li>
      <li><i>Edit Product</i> to edit an existing product that may be chosen in adding an order/transaction to the database</li>
      <li><i>Delete Product</i> to delete an existing product within the available products' database</li>
      <li><i>View Sold Items Database</i> to view a database of the transactions created.</li>
      <li><i>View Products Database</i> to view a database of the products offered to be sold.</li>
      <li><i>View Raw Materials Database</i> to view a database of the raw materials used for the creation of products.</li>
    </ol>
  <li>User may logout of the site.</li>
</ol>
<b>Setting up a Local Database</b>
<ol>
  <li>From PyCharm, access the right-side of the IDE entitled <i>Database</i>
  <li>Find the "+" icon on the menubar of the window and press <i>Data Source</i>, and <i>PostgreSQL</i>
  <li>Change the Database textfield to your desired name for your database </li>
  <li>Add a user and password for your database for ease of access</li>
  <li>Click Test Connection to see if your database is running</li>
  <li>Press Apply and OK to continue</li>
</ol>

  
  ## Revision Logs and Version History
  
  * 1.8
    * Data visualization is now implemented in the program.
    * Revised the program's overall color-scheme.
  * 1.7
    * All user cases were implemented in the program.
    * The CSS designs are formatted along with the layout of the back-end functions.
  * 1.6
    * Modularized functions in accordance to their primary task.
    * Revised functions under the products module to be executed under PostgreSQL.
  * 1.5
    * Refined UI for registration page.
    * Defined additional functions for login and registrations.
    * Connected the remaining views.py functions to the necessary html pages.
  * 1.4
    * Migrated from SQLite to PostgreSQL.
    * Usability of forms within the html files.
    * Initial design and functionality of login and registration pages.
  * 1.3
    * Created functions under views.py of the <i>pages</i> module.
    * Linked the html files to the corresponding views.py functions.
    * Initial CSS designs appended.
    * Django Admin and SQLite utilized in adding <i>products</i>.
  * 1.2
    * Created the necessary html pages.
  * 1.1
    * Revised overall structure of the modules.
  * 1.0
    * Initial setup of PyCharm localhost website.

### Authors and Contributions

#### Arciella Brience C. Crisostomo [arciella_brience_crisostomo@dlsu.edu.ph]
* Back-end developer.
* Researches the built-in functions available within PyCharm, along with the necessary packages needed in the program's overall execution.
* Integrates the necessary functions involving data appending and data retrieval for Django and PostgreSQL.

#### Dustin Kyle D. Landicho [dustin_kyle_landicho@dlsu.edu.ph]
* Front-end developer.
* Handles the program layout through the research and creation of CSS files, as well as utilizing available Bootstrap sources and JavaScript files.
* Spearheaded the design-phase through Figma development. 
  
#### John Emmanuel E. Pareja [j-em_pareja@dlsu.edu.ph]
* Back-end developer.
* Created the overall flow of the program, including the skeletal structure of the functions necessary in each page along with the necessary html components.
* Tested and modularized the functions necessary in the execution of the program.
