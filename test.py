from translate import Translator
translator = Translator(to_lang="German")
translation = translator.translate(input())
print(translation)