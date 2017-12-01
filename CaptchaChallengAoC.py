def addCaptcha(captcha):
  try: int(captcha)
  except: return ('NaN')
  
  final = 0
  captchaStr = str(captcha)
  for i in range(-1,len(captchaStr)-1):
    if captchaStr[i] == captchaStr[i+1]:
      final += int(captchaStr[i])
  
  return final

