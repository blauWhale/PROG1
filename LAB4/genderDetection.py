import re

# 2.2.1 Function to count first-person singular pronouns
def count_first_person_pronouns(text):
    pronouns = ['i', 'me', 'my']
    # Split text into words and convert to lowercase for case-insensitive matching
    words = re.findall(r'\b\w+\b', text.lower())
    count = sum(1 for word in words if word in pronouns)
    return count

# 2.2.2 Function to compute the number of words in the text
def document_length(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# 2.2.3 Function to compute the average number of words per sentence
def average_words_per_sentence(text):
    sentences = re.split(r'[.!?]', text)  # Split text by sentence-ending punctuation
    sentences = [sentence for sentence in sentences if sentence.strip()]  # Remove empty sentences
    num_words = document_length(text)
    return num_words / len(sentences) if sentences else 0

# 2.2.4 Function to detect gender based on rules
def gender_detection(text):
    pronoun_count = count_first_person_pronouns(text)
    word_count = document_length(text)
    avg_words_per_sentence = average_words_per_sentence(text)

    # Basic rule of thumb for gender detection
    if pronoun_count > 10 or word_count > 150:
        return "female"
    elif avg_words_per_sentence > 20 and word_count < 100:
        return "male"
    else:
        return "unknown"
        
# Example usage
sample_text = """
I think that my experiences have shaped who I am today. My opinions and thoughts are deeply personal.
I believe that every journey starts with a step.
"""

print("Number of first-person singular pronouns:", count_first_person_pronouns(sample_text))
print("Document length (number of words):", document_length(sample_text))
print("Average number of words per sentence:", average_words_per_sentence(sample_text))
print("Gender detection result:", gender_detection(sample_text))
