import pyotp
import sys
import qrcode
from PIL import Image

'''
SOURCES: 
https://pyauth.github.io/pyotp/#:~:text=secret-,Google%20Authenticator%20Compatible
https://pypi.org/project/qrcode/  
    ^ specifically: 'Advanced Usage: QRCode class' & 'Pure Python PNG'
https://tools.ietf.org/html/rfc6238
https://pillow.readthedocs.io/en/stable/
'''


userEmail = 'example@google.com'
issuerName = 'Secure App'
secret_hc = 'CFBXIOH2AHXUXVZI35MUTYQHM4IGJ65X'      # hard-coded secret (one instance/return value from gen_secret())
totp_uri = pyotp.totp.TOTP(secret_hc).provisioning_uri(name=userEmail, issuer_name=issuerName)


def gen_secret():
    """
    gen_secret() -- generates a 32-character base32 secret compatible with Google Authenticator and other OTP apps.
    - program currently uses hard-coded value for secret.
    - value of secret_hc can be replaced with call to gen_secret() to generate a new secret with each call.

    takes no parameters
    :return: random base32 number """
    base32 = pyotp.random_base32()
    return base32


def gen_otp():
    """
    finds TOTP assigned for current 30-second interval and prints the value
    source: https://pyauth.github.io/pyotp/#:~:text=secret-,Google%20Authenticator%20Compatible

    takes no parameters
    :return: nothing
    """
    totp = pyotp.TOTP(secret_hc)
    now = totp.now()
    print(f'totp: {now}')


def gen_qr():
    """
    generates QR code, adds data to QR code, and creates .jpg with QR code data.
    source: https://pypi.org/project/qrcode/  (specifically: 'Advanced Usage: QRCode class' & 'Pure Python PNG')

    takes no arguments
    :return: nothing
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    totp = pyotp.TOTP(secret_hc)
    qr.add_data(totp_uri)

    # create PilImage object
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('otp-qr.jpg')

    # print(f'img type: {type(img)}')
    # print(f'img size: {img.size}')

    # create image object & open in separate window
    img_open = Image.open(r"otp-qr.jpg")
    img_open.show()


# check user input ; call specified method or print error statement
program = sys.argv[0]

if len(sys.argv) > 1:
    # print(f'secret: {gen_secret()}')
    arg = sys.argv[1]
    if arg == '--get-otp':
        gen_otp()
        exit()
    elif arg == '--generate-qr':
        gen_qr()
        exit()
    else:
        print("ERROR: COMMAND UNKNOWN")
print("MUST SPECIFY: \n --get-otp \n    OR \n --generate-qr")
