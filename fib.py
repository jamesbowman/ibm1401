code = [
  "/332",
  "/",
  ",216",
  "A080220",
  "2",
  "B0592160",
  "."
  ""
]

card = bytearray("!" + (80 * " "))

org = 1 + len(code) * 7
for i,c in enumerate(code):
    card[7*i+1:7*i+8] = ",%03d%03d" % (7*i+8, org)
    card[org:org+len(c)] = c
    org += len(c)
card[76:81] = "01111"
print card[1:]
print "    ^    1    ^    2    ^    3    ^    4    ^    5    ^    6    ^    7    ^    8"

open("fib.cd", "w").write(card[1:] + "\n")
