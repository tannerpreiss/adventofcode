import sys

if len(sys.argv) < 2:
   print("Correct use : 'python paper_amt.py <input_file>'")
   exit();

filename = sys.argv[1]
total_paper = 0

words = open(filename).read().split()
for word in words:  		
  measurements = word.split("x")
  l = int(measurements[0])
  w = int(measurements[1])
  h = int(measurements[2])
  s1 = l * w
  s2 = l * h
  s3 = w * h
  cur_gift = 2 * (s1 + s2 + s3) + min(s1, s2, s3)
  total_paper += cur_gift

print "The elves need a total of " + str(total_paper) + " square feet of wrapping paper."