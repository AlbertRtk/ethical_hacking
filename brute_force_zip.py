import zipfile
from tqdm import tqdm

""" User's input """
ZIP_FILE_PATH = r'C:\Users\Albert\Albert\projects\python\ethical_hacking\test.zip'
DICT_FILE_PATH = r'C:\Users\Albert\Albert\projects\python\ethical_hacking\brute_force_dict\rockyou.txt'


def brute_force_zip(zip_file, dict_file):
    """
    Brute force attack on password protected zip file.

    :param zip_file: path to zip file to be attacked
    :param dict_file: txt file with list of passwords
    :return: found password or None if password was nit found
    """
    with open(dict_file, 'r', encoding='utf-8', errors='replace') as f:
        pwd_list = f.read().split('\n')

    with zipfile.ZipFile(zip_file) as zf:
        for next_pwd in tqdm(pwd_list):
            password = next_pwd.strip()
            try:
                zf.extractall(pwd=bytes(password, encoding='utf-8'))
            except:
                pass
            else:
                return password


if __name__ == '__main__':
    found_pwd = brute_force_zip(ZIP_FILE_PATH, DICT_FILE_PATH)

    if found_pwd:
        print(f'Password found: {found_pwd}')
    else:
        print('Password not found :-(')
