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


def process_record(data: list[str]) -> list[str]:
    good_records = []
    bad_records = []

    for record in data:
        search_errors_record = re.search(r"#|NULL|null|[-]\d*", record)
        valid_phone_number = re.search(r"(\d{10})", record)
        valid_amount_error = re.findall(r"[-]?\d+", record)  # enleve les crochets si tu veux
        neg_and_zero_amount_error = valid_amount_error[1]
        convert_to_integer = int(neg_and_zero_amount_error)
        # print((convert_to_integer))
        try:
            if search_errors_record or not valid_phone_number or convert_to_integer <= 0:
                bad_records.append(record)
                continue
            else:
                good_records.append(record)
                # print(good_records)
        except Exception as e:
            print("This is the error:", e)

    return bad_records, good_records  # I return 2listes in a -> tuple


# result = process_record(data_copy) # I return 2listes in a -> tuple
# print(result) # # I return 2listes in a -> tuple
# bad_records, good_records = process_record(data_copy) # Je decompresse le tuple en deux listes
# print("GOOD R :", good_records)
# print("BAD R :", bad_records)
#
print("\n" * 1)
print(f"    {'2. USE ASSERT -> Ensure: User name is not NULL, Amount > 0'}")
print("=" * 140)


def assert_use(data: list[str]) -> list[str]:
    null_user = []
    for record in data:
        search_null_user = re.search(r"NULL|null", record)
        positive_amount = re.findall(r"[-]?\d+", record)
        conv_pos_amount_to_int = int(positive_amount[1])
        print(conv_pos_amount_to_int)
        if search_null_user or conv_pos_amount_to_int <= 0:
            null_user.append(record)
    # raise ValueError ('Username must not be NULL')
    assert search_null_user is None or conv_pos_amount_to_int <= 0, f"NULL value is not allowed {null_user}"
    return null_user


# result = assert_use(data_copy)
# print(result)


#
#
print(
    f"    {'3. REGEX EXTRACTION -> Extract:name, phone (valid 10 digits only), email (valid format), amount (only numbers)'}")
print("=" * 140)


def extraction_data(data: list[str]) -> list[str]:
    name_extracted = []
    phone_extracted = []
    email_extracted = []
    amount_extracted = []
    for record in data:
        email_search = re.findall(r"\w+@\w+.\w+", record)
        phone_search = re.search(r"\d{10}", record)
        amount_search = re.findall(r"[-]?\d+", record)
        # name_search = re.search(r"\w+[^0-9]", record)
        if email_search:
            email_extracted.append(email_search)
        if phone_search:
            phone_extracted.append(phone_search.group())
        if amount_search:
            amount_extracted.append(amount_search[1])
        # if name_search:
        #     name_extracted.append(name_extracted)

    return name_extracted, phone_extracted, email_extracted, amount_extracted # this a tuple so i will unpress it to list


name_extracted, phone_extracted, email_extracted, amount_extracted = extraction_data(data_copy)
print(f"NAME_EXTRACTED: {name_extracted}") # list after i unpress
print(f"PHONE_EXTRACTED: {phone_extracted}") # list after i unpress
print(f"EMAIL_EXTRACTED: {email_extracted}") # list after i unpress
print(f"AMOUNT_EXTRACTED: {amount_extracted}") # list after i unpress



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


# text = "call me at 971555154764 or erman@gmail.com"

# print(re.findall(r"\d+",text))
# print(re.search (r"\w+@\w+.\w+",text))




