import pywhatkit

text = '''my name is vikas.
i am 19 years old
i lived in mohan gerden new delhi'''

hand_write = pywhatkit.text_to_handwriting(text)
print(hand_write)