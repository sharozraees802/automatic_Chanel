from gtts import gTTS
eng = "تفصیلات کے مطابق سوڈان کے شمالی صوبہ دارفور میں ایک خوفناک ٹریفک حادثہ پیش آی ، سڑک حادثے میں کم از کم 57 افراد کی ہلاکت کی اطلاعات موصول ہوئی ہیں۔"
obj=gTTS(text=eng,slow = False ,lang='ur')
obj.save('urdu.mp3')