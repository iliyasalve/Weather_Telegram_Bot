from translate import Translator

def translate_message(text: str, lang: str) -> str:
    '''
    Returns translated text from English to the selected language
    '''

    translator= Translator(from_lang="en", to_lang=lang)

    translated_text = translator.translate(text)

    return(translated_text)
