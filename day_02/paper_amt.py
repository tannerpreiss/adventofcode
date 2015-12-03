import sys

if len(sys.argv) < 2:
   print("Correct use : 'python paper_amt.py <input_file>'")
   exit();

filename = sys.argv[1]
total_paper, total_ribbon = 0 , 0

words = open(filename).read().split()
for word in words:  		
  l , w , h = map(int, word.split("x"))
  s1, s2, s3 = l * w, l * h, w * h
  total_paper += 2 * (s1 + s2 + s3) + min(s1, s2, s3)
  total_ribbon += 2 * min(l+w, l+h, w+h) + (l*w*h)

print("The elves need a total of " + str(total_paper) + " square feet of wrapping paper.")
print("The elves need a total of " + str(total_ribbon) + " feet of ribbon.")

