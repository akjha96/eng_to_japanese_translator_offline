from translate import Translator


def translate_to_japanese(line_to_convert):
    translator = Translator(to_lang='ja')
    translation = translator.translate(line_to_convert)
    return translation


while True:
    try:
        with open('english.txt', mode='a') as english_to_japanese_file:
            text = input("Please enter your sentence in english: ")
            print(f"English: {text}", file=english_to_japanese_file)
            print(f"Japanese: {translate_to_japanese(text)}",
                  file=english_to_japanese_file)

        with open('english.txt', mode='r') as converted_file:
            for line in converted_file:
                print(line)
        enter_next_text = input("Do you want to continue? Y/N: ")
        enter_next_text = enter_next_text.lower()

    except Exception as ex:
        print(f"Found error!! {ex}")

    else:
        if enter_next_text.upper() == 'Y':
            continue
        else:
            break
