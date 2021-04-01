import requests
import hashlib
import sys
# API koristi hashing
# Kanonimiti - da primi info o nama a da ne zna ko smo,
# damo prvih 5 karaktera
# prvo je response sa celim hesom bio 400, sa 5 karatera 200


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    print(url)
    resposne = requests.get(url)
    print(resposne)
    if resposne.status_code != 200:
        raise RuntimeError('eror')
    return resposne


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check pass if exists in api response
    # haslib, sha1 koristimo, hexdigest heksadecimalni brojevi
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1password)
    first5_char, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first5_char)
    print(first5_char, tail)
    print(res)
    return get_password_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print("nadjen")
        else:
            print("nije nadjen")
    return 'done!'


# da ce se pokrenuti ako je main file
if __name__ == '__main__':
    # sys.exit da se zavrsi ako ima problem, sa tim se vraca 'done!'
    sys.exit(main(sys.argv[1:]))
