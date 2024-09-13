import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from docx import Document
import stack
import pyautogui,time,pyperclip
from doc import fname



def summarize(text, summary_length):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Get the frequency of each word
    freq = FreqDist(words)

    # Get the stopwords
    stop_words = set(stopwords.words('english'))

    # Calculate the score of each sentence
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word not in stop_words:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq[word]
                else:
                    sentence_scores[sentence] += freq[word]

    # Sort the sentences by score
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    # Create the summary
    summary = ''
    for sentence, score in sorted_sentences:
        if len(summary.split()) < summary_length:
            summary += sentence + ' '

    return summary.strip()

def append_text_to_doc(text):
    
    name= fname()
    doc = Document(name)
    doc.add_paragraph(text)
    doc.save(name)
    stack.set_action(text)
    print(f"Appended text: {text}")

def summarizer(parent):
    parent.destroy()
        # Download required NLTK data
    nltk.download('punkt_tab')
    nltk.download('punkt')
    nltk.download('stopwords')
    
    # Copy the selected text to the clipboard (assumes the user has selected text)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    selected_text = pyperclip.paste()
    
    summary_length = 200
    output=summarize(selected_text,summary_length)
    print(summarize(selected_text, summary_length))
    append_text_to_doc(output)
    