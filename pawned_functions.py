import requests
import hashlib


def get_user_input():
    user_input = input("Enter a password: ")
    user_password = user_input

    return prep_input_with_hashlib(user_password)


def prep_input_with_hashlib(pass_text):
    pass_to_hashlib = hashlib.sha1(f"{pass_text}".encode()).hexdigest().upper()
    first5_hashlib = pass_to_hashlib[:5]
    five_to_end_hashlib = pass_to_hashlib[5:]

    return call_the_api(the_user_pass=pass_text,
                        five2e=five_to_end_hashlib,
                        f5=first5_hashlib,
                        full_hd=pass_to_hashlib)


def call_the_api(the_user_pass, five2e, f5, full_hd):
    url = f"https://api.pwnedpasswords.com/range/{f5}"
    api_response = requests.get(url=url)
    # print(api_response)
    line_splitter = api_response.text.splitlines()

    return check_and_filter(text_password=the_user_pass, api_split=line_splitter, f2e=five2e)


def check_and_filter(text_password, api_split, f2e):
    for line in api_split:
        new_line = line.split(":")
        api_response_list = []
        api_response_list.append(new_line)

        for hex_d, count in api_response_list:
            if hex_d in f2e:
                print(
                    f"The password {text_password} appears in {count} data breaches.")
                return f"The password {text_password} appears in {count} data breaches."
    print(
        f"The password {text_password} appears to be good to go, Rock and Roll!")
    return f"The password {text_password} appears to be good to go, Rock and Roll!"


get_user_input()
