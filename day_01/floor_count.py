import sys

if len(sys.argv) < 2:
   print("Correct use : 'python floor_count.py <input_file>'")
   exit();

filename = sys.argv[1]
floorcount = 0
position = 0
entered_basement = False

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if c == "(":
      floorcount += 1
    if c == ")":
      floorcount -= 1
    if not entered_basement:
      position += 1
      if floorcount < 0:
        entered_basement = True
 
print("Santa entered the basement on position " + str(position))
print("Santa ended on floor " + str(floorcount))
