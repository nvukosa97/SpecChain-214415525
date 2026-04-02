"""cleans raw data & make clean dataset"""
import json
import re
import string
from pathlib import Path

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from num2words import num2words

# Download NLTK resources once
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def remove_emojis(text):
    # Remove most emoji / pictograph unicode ranges
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub("", text)


def numbers_to_text(text):
    def replace_number(match):
        num = match.group()
        try:
            return num2words(int(num))
        except:
            return num
    return re.sub(r"\b\d+\b", replace_number, text)


def clean_review_text(text):
    if not text:
        return ""

    # lowercase
    text = text.lower()

    # convert numbers to words
    text = numbers_to_text(text)

    # remove emojis
    text = remove_emojis(text)

    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # remove special characters, keep letters and spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # tokenize
    tokens = text.split()

    # remove stop words + lemmatize
    cleaned_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stop_words
    ]

    return " ".join(cleaned_tokens)


BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "reviews_raw.jsonl"
output_file = BASE_DIR / "data" / "reviews_clean.jsonl"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for i, line in enumerate(infile, start=1):
        review = json.loads(line)

        cleaned_review = {
            "review_id": f"rev_{i}",
            "cleaned_content": clean_review_text(review.get("content", "")),
            "score": review.get("score", None)
        }

        json.dump(cleaned_review, outfile, ensure_ascii=False)

        outfile.write("\n")

print(f"Cleaned reviews saved to {output_file}")