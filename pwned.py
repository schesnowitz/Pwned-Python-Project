import requests
import hashlib


user_password = "steveDDDDDDDDDDDDDDDDDDDDDDDDD"

pass_to_hashlib = hashlib.sha1(f"{user_password}".encode()).hexdigest().upper()
first5_hashlib = pass_to_hashlib[:5]
five_to_end_hashlib = pass_to_hashlib[5:]
# print(pass_to_hashlib)
# print(first5_hashlib)
# print(len(five_to_end_hashlib))
# print(len("EA3407B43D3E7F8D6F25E1F37307F9C4AA2"))
url = f"https://api.pwnedpasswords.com/range/{first5_hashlib}"

api_response = requests.get(url=url)

# print(type(api_response.text))
line_splitter = api_response.text.splitlines()

# print(type(strip_api_res_text))


for line in line_splitter:
    new_line = line.split(":")

    api_response_list = []
    api_response_list.append(new_line)
    # print(api_response_list)

    for hex_d, count in api_response_list:
        # print(hex_d)
        # print(count)

        if hex_d in five_to_end_hashlib:
            print(
                f"The password {user_password} appears in {count} data breaches.")

print(f"The password {user_password} appears to be good to go, Rock and Roll!")
