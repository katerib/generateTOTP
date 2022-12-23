# TOTP
Time-based One-Time Password Generator for use with Google Authenticator

## About otp.py

Generates a 30-second [time-based one time password (TOTP)](https://tools.ietf.org/html/rfc6238) to be used with [Google Authenticator (GA)](https://github.com/google/google-authenticator). 

Generate QR Code: `--generate-qr`

* Generates a QR code compatible with Google Authenticator (encodes the URI expected by GA)
* URI contains secret keys (hard-coded) and user ID (hard-coded) required for the TOTP algorithm
* QR code saved to the parent directory as a .JPG image with filename 'otp-qr.jpg' (overwrites current file if present, otherwise creates new file)
* Usage: First called to set up GA and generate QR code

Get OTP (TOTP): `--get-otp`

* Prints current 30-second OTP to the console using the call `totp.now()`
* Usage: Can be called as often as needed ; OTP will regenerate every 30 seconds
## Installation

Use pip to install the required packages as outlined in `\requirements.txt`.

Run ```bash pip install -r requirements.txt``` OR install each package separately:
* pip install pyotp
* pip install qrcode
* pip install pillow

## Usage

Two arguments can be passed to the program in the following order via the command line:

```bash
[exe] --generate-qr  # generates QR code as .jpg and opens image

[exe] --get-otp  # prints current TOTP to console
```

Where `[exe]` is the call to the program, such as `./otp.py` or `py otp.py`



### NOTE

>> This program works with the Google Authenticator mobile app. Download the app from the App Store for IOS or Android devices.
