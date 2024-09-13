from deep_translator import GoogleTranslator
import pyautogui,time,pyperclip
from doc import fname
from docx import Document
import stack


def translate_text(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    sentences = text.split('. ')
    translated_sentences = []
    
    for sentence in sentences:
        if len(sentence) > 0:  # ignore empty sentences
            translation = translator.translate(sentence)
            translated_sentences.append(translation)
    
    translated_text = '. '.join(translated_sentences)
    return translated_text

def append_text_to_doc(text):
    
    name= fname()
    doc = Document(name)
    doc.add_paragraph(text)
    doc.save(name)
    stack.set_action(text)
    print(f"Appended text: {text}")

def translator(parent):
    parent.destroy()
    
    # Copy the selected text to the clipboard (assumes the user has selected text)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    text_to_translate = pyperclip.paste()
    # Example usage:
    
    target_language = "hi"  # hindi
    translated_text = translate_text(text_to_translate, target_language)
    print(f"Translated text: {translated_text}")
    append_text_to_doc(translated_text)