import time

print("scrapping data...")
time.sleep(3)
with open('./posts.json', 'w') as fp:
	fp.write("[some posts in json!]")
print("finished scrapping!")