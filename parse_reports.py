import time

print("parsing reports...")
time.sleep(2)
with open("reports.json", 'w') as fp:
	fp.write("[some reports yay!]")
print('wrote reports...')
time.sleep(1)
print("done parsing reports")
