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
        search_errors_record = re.search(r"#|NULL|null|[-]\d*", record)
        valid_phone_number = re.search(r"(\d{10})", record)
        valid_amount_error = re.findall(r"[-]?\d+", record) # enleve les crochets si tu veux
        neg_and_zero_amount_error = valid_amount_error[1]
        convert_to_integer = int(neg_and_zero_amount_error)
        # print((convert_to_integer))
        try:
            if search_errors_record or not valid_phone_number or convert_to_integer<=0 :
                bad_records.append(record)
                continue
            else:
                good_records.append(record)
                print(good_records)
        except:
            pass

    return bad_records, good_records # I return 2listes in a -> tuple
# result = process_record(data_copy) # I return 2listes in a -> tuple
# print(result) # # I return 2listes in a -> tuple

bad_records, good_records = process_record(data_copy) # Je decompresse le tuple en deux listes
print("GOOD R :", good_records)
print("BAD R :", bad_records)
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

# print(re.search(r'\d<0','Amount:Rs.0'))
# print(re.search(r'\d<0','Amount:Rs.5000'))
# pos = re.search(r'\d+','Amount:Rs.7000')
# print(pos.group())
# if int(pos.group()) >=0:
#     print("+ positif")
#


# def test():
#     a = [1, 2, 3]
#     b = [4, 5, 6]
#
#     return a, b
#
# a, b = test()
#
# print(a)
# print(b)