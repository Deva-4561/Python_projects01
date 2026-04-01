emails = set()

n = int(input("Enter number of emails: "))

for i in range(n):
    email = input("Enter email: ")
    
    if email in emails:
        print("Duplicate email found")
    else:
        emails.add(email)

print("Unique Emails:", emails)