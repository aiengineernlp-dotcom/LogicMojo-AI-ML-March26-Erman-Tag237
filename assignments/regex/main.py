import re
data = ["User: Mahipal | Phone: 9876543210 | Email: mahi@gmail.com | Amount: Rs.5000",
        "User: Ravi | Phone: 98765abc10 | Email: ravi#gmail.com | Amount: USD300",
        "User: NULL | Phone: 9123456789 | Email: test@yahoo.com | Amount: Rs.7000",
        "User: Ankit | Phone: 9999999999 | Email: ankit@gmail.com | Amount: Rs.0",
        "User: Sita | Phone: 8888888888 | Email: sita@gmail.com | Amount: Rs.-100"
       ]
# copy of the dataset for later comparaison :
data_copy = data[:]
data.append("lol")
print(data_copy)
print("\n")
print(data)
print("\n")
print(f"    {'1.HANDLE EXCEPTIONS: Safely process each record, Skip bad records but log errors'}")
print("=" * 140)

def process_record(data:list) -> list:
    good_records = []
    bad_records = []

    for record in data:
        search_errors_record = re.search(r"#|NULL|null|[-]\d*|", record)
        valid_phone_number = re.search(r"(\d{10})", record)
        # valid_amount =
        try:
            if search_errors_record or not valid_phone_number or:
                bad_records.append(record)
                continue
            else:
                good_records.append(record)
                #print(good_records)
        except:
            pass
    return bad_records





"""
. 
^
$
*
+
[]
{}
?
\
======
re.search()
re.findall()
re.match()
re.sub()
re.split()

"""



d = process_record (data_copy)
print(d)
print("\n")
#
# print(f"    {'2. USE ASSERT -> Ensure: User name is not NULL, Amount > 0'}")
# print("=" * 140)
#
#
# print(f"    {'3. REGEX EXTRACTION -> Extract:name, phone (valid 10 digits only), email (valid format), amount (only numbers)'}")
# print("=" * 140)
#
# print(f"    {'4. ADVANCED REGEX -> Extract currency: Rs,USD'}")
# print("=" * 140)
# print(f"    {'5. STRING CLEANING -> lowercase everything, remove special characters'}")
# print("=" * 140)
# print(f"    {'6. FINAL OUTPUT -> Return clean structured dataset:'}")
# """
# [{‘name’: ‘mahipal’, ‘phone’: ‘9876543210’, ‘email’: ‘mahi@gmail.com’, ‘amount’: 5000, ‘currency’: ‘rs’},...]
# """
# print("=" * 140)
#
#
# import re
# print(re.search(r"\d<=0", "Amount: Rs.0"))
# print(re.search(r"\d<=0", "Amount: Rs.5000"))
#
# amounts = [
#     "Amount: Rs.5000",
#     "Amount: Rs.0",
#     "Amount: Rs.-100",
#     "Amount: USD300"
# ]
# for a in amounts:
#     match = re.search(r"[-]?\d+",a)
#     # print(match.group())
#     if int(match.group()) <= 0:
#         print(match.group())



amounts = [
    "Amount: Rs.5000",
    "Amount: Rs.0",
    "Amount: Rs.-100",
    "Amount: USD300"
]

for a in amounts:
    match = re.search(r"[-]?\d+", a)
    if int(match.group()) <= 0:
        print(f"INVALIDE : {a}")
    else:
        print(f"VALIDE   : {a}")