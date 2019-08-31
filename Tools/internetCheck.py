from urllib.request import urlopen
def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        print("There is internet")
        return True
    except:
        print('No Internet')
        return False
internet_on()