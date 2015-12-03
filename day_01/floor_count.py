import sys

if len(sys.argv) < 2:
   print("Correct use : 'python floor_count.py <input_file>'")
   exit();

filename = sys.argv[1]
floorcount = 0

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if c == "(":
      print("going up")
      floorcount += 1
    if c == ")":
      print("going down")
      floorcount -= 1

print("Santa ended on floor " + str(floorcount))
