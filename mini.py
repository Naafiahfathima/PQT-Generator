n=int(input("Enter a number:"))
while (n==1):
    import random
    pass_len = int(input("Enter the length of the password: "))
    pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
    password = "".join(random.sample(pass_data, pass_len))
    print(password)
    break;
if (n == 2):
    import qrcode
    link = input("Enter link :")
    img = qrcode.make(link)
    img.save("test.png")
elif(n==3):
    from gtts import gTTS
    from playsound import playsound
    audio = "speech.mp3"
    language = 'en'
    Text = input("Enter text which you want to convert into audio file: ")
    sp = gTTS(text=Text, lang=language, slow=False)
    sp.save(audio)
    playsound(audio)




















