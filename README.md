# Happy Number
A little Python3 function that determines if a number is a happy number. 

[What's a happy number?](http://en.wikipedia.org/wiki/Happy_number)

Insipred by: http://www.smashcompany.com/technology/embarrassing-code-i-wrote-under-stress-at-a-job-interview

# Sample Usage


```shell-session
$ python3.4 happy.py 
usage: happy.py <integer>
```
```shell-session
$ python3.4 happy.py 5
unhappy number
```
```shell-session
$ python3.4 happy.py 7
happy number
```
```shell-session
$ python3.4 happy.py 1
happy number
```
```shell-session
$ python3.4 happy.py 0
input must be greater than 0
```
```shell-session
$ python3.4 happy.py -9
input must be greater than 0
```
```shell-session
$ python3.4 happy.py dfg
input is not an integer
```
```shell-session
$ python3.4 happy.py 998
happy number
```
```shell-session
$ python3.4 happy.py 555
unhappy number
```
