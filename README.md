# Omark

Omark is the new form of taking attendance in class, its captures a classroom and determines which student is in class and which student isn't

# Overview
The Omark Program was written with fast use in mind. It provides the following key features

  - Returns a list of total students in class
  - Returns a list of students absent from class
  - Returns a list of students present in class
 


## Usage

In the following paragraphs, I am going to describe how you can get and use Omark.

###  Getting it

To download Omark , either fork this github repo or simply use Pypi via pip, install Omarke.
```sh
$ pip install Omarke
```

### Using it

First, import Omark from Omark

```Python
from Omark import Omark 
```

 
## Initialize Omark
First, let's create a new Omark object. For this , just provide the students in a text file and a folder of all the students image with the names saved as the same name stored in the text file.

```Python
 
om = Omark(students='file.txt',data='folder')

```
## View all details
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.register())


```
## View all students
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.students)


```
## View all absent students
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.absent)


```

 ## View all present students
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.present)


```
 ## 
 

```Python
 
from Omark import Omark 
om = Omark(students='file.txt',data='folder')
print(om.register())
print(om.absent)
print(om.present)

```


License
----

MIT License

Copyright (c) 2021 Teddy Oweh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Hire me: `teddyoweh`
