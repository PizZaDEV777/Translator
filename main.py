from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    print("Simple Language Translation System")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Enter text to translate: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        target_language = input("Enter target language (e.g., 'es' for Spanish): ")
        
        try:
            translated_text = translate_text(user_input, target_language)
            print(f"Translated text: {translated_text}")
        except Exception as e:
            print(f"Translation error: {e}")

if __name__ == "__main__":
    main()