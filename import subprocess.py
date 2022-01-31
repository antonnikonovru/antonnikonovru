import subprocess

def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
    print(profiles_data)

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile{profile} key=clear').decode('utf-8').split('\n')
        # print(profile_info)
        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key content' in i]
        except IndexError:
            password = None

        print(f'profile: {profile}\nPassword: {password}\n{"#" * 20}')

extract_wifi_passwords()