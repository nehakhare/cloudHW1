DESCRIPTION
The website gives lets you to check whether the number you enter is a palindrom or not(A number is a palindrom if it can br read same from left and right side ].Example:12321).
The programming part of the project uses HTML, CSS and Python. 
The number you enter is send to the server-side Python which processes the number and checks it and gives you the output. It uses POST method to accept  input.
The code of the following was uploaded to the EC2 in the var/www/html where I made a folder named main where my Python program is stored under the name main.py. 
I have also created folder named templates which stores my HTML File and static folder which has my CSS file.
Also, I have setup Python with a WSGI server.
For doing this I made changes in the httpd.conf file and added code to it and made a .wgsi file whichcontains the path to the Python to integrate WSGI server.
