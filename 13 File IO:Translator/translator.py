from deep_translator import GoogleTranslator

try:
    with open('/translator.txt', mode='r') as moj_fajl:
        text = moj_fajl.read()
        print(text)
        translate = GoogleTranslator(
            source='auto', target='zh').translate(text)
        print(translate)
        with open('/translator2.txt', mode='w') as moj_fajl2:
            moj_fajl2.write(translate)
except FileNotFoundError as e:
    print('nema fajla')
