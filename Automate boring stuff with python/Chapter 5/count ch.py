import pprint
message = 'It was bright cold day in April, and the clocks were striking thirteen.'
count = {}

for ch in message:
        count.setdefault(ch, 0)
        count[ch] = count[ch]+ 1
pprint.pprint(count)
