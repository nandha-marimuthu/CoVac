from captcha.image import ImageCaptcha
def capt():
    image = ImageCaptcha(width = 250, height = 80)
    otp = 'covac' 
    data = image.generate(otp)
    image.write(otp, 'capt.png')
    return otp

