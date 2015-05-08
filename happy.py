import sys

if len(sys.argv) != 2:
  print("usage: " + sys.argv[0] + " <integer>")
  exit(1)

try:
  n = int(sys.argv[1])
except ValueError:
  print("input is not an integer")
  exit(2)

if n <= 0:
  print("input must be greater than 0")
  exit(3)

def happy(n):
  l = []
  sum = 0
  for digit in str(n):
	sum += int(digit)**2
  l.append(sum)
  for i in l:
	sum = 0
	for digit in str(i):
	  sum += int(digit)**2
	l.append(sum)
	if sum == 1:
	  return "happy number"
	if l.count(i) > 1:
	  return "unhappy number"

print(happy(n))
