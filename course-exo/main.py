data = [
    "User: Mahipal | Phone: 9876543210 | Email: mahi@gmail.com | Amount: Rs.5000",
    "User: Ravi | Phone: 98765abc10 | Email: ravi#gmail.com | Amount: USD300",
    "User: NULL | Phone: 9123456789 | Email: test@yahoo.com | Amount: Rs.7000",
    "User: Ankit | Phone: 9999999999 | Email: ankit@gmail.com | Amount: Rs.0",
    "User: Sita | Phone: 8888888888 | Email: sita@gmail.com | Amount: Rs.-100"
]

1. HANDLE EXCEPTIONS
Safely process each record Skip bad records but log errors

2. USEASSERT
Ensure: User name is not NULL Amount > 0

3. REGEX EXTRACTION
Extract:
    - name phone (valid 10 digits only)
    - email(valid format)
    - amount(only numbers)

4. ADVANCED REGEX
Extract 
    - currency:
    - Rs
    - USD

5. STRING CLEANING
- lowercase
- everything
- remove
- special
-= characters

6.FINAL OUTPUT
Return
clean
structured
dataset: [ {'name': 'mahipal', 'phone': '9876543210', 'email': 'mahi@gmail.com', 'amount': 5000, 'currency': 'rs'},...]