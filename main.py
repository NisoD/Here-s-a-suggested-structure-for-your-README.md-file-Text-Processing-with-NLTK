import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import matplotlib.pyplot as plt
from collections import Counter
import re
from nltk.stem import SnowballStemmer
import click
from wordcloud import WordCloud


@click.command()
@click.option('--file', default='sherlock_holmes.txt', help='The file to process')
def main(file):
    """ reads a text file and creates tag cloud and explores word count occurnces """
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    with open(file, 'r', encoding='utf8') as data:
        text = data.read()
    

    tokens = word_tokenize(text.lower())
    tokens = remove_symbols(tokens)
    
    process_and_plot(tokens, "Original")
    
    tokens_no_stopwords = remove_stopwords(tokens)
    process_and_plot(tokens_no_stopwords, "Without Stopwords")
    
    stemmed_tokens = stem_tokens(tokens_no_stopwords)
    process_and_plot(stemmed_tokens, "Stemmed")
    
    tagged_tokens = pos_tag(tokens_no_stopwords)
    # print_20_examples_pos(text) 'in order to find a mistake  uncomment that
    proper_nouns = [token for token,
                    tag in tagged_tokens if tag in ('NNP', 'NNPS')]
    create_wordcloud(proper_nouns, "Proper Nouns Tag Cloud")
    repeated_words = find_repeated_words(text)
    print(f'repeated_words: {repeated_words}')


def print_20_examples_pos(text):
    sentences = sent_tokenize(text)
    count = 0
    for sentence in sentences:
        if count >= 20:
            break
        tokens = word_tokenize(sentence)
        tags = pos_tag(tokens)
        print(f"Sentence {count + 1}: {sentence}")
        print("POS Tags:", tags)
        print("\n")
        count += 1


def create_wordcloud(words, title):
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(' '.join(words))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()
    plt.savefig(title + '.png')


def find_repeated_words(text, toprint=False):
    # word boundry,one or more chars,word boundry,one or more whitespaces,back ref for the previous word that repeated,
    pattern = re.compile(r'\b(\w+)\b[^\w\n]*\b\1\b', re.IGNORECASE)
    sentences = sent_tokenize(text)
    repeated_words = []
    for sentence in sentences:
        matches = pattern.findall(sentence)
        if matches:
            repeated_words.extend(matches)
            if toprint:
                print(f"Sentence with repeated words: {sentence}")
                print(f"Repeated words: {', '.join(matches)}\n")
    return set(repeated_words)


def remove_symbols(tokens):
    pattern = re.compile(r'^[a-z0-9]+$')
    return [token for token in tokens if pattern.match(token)]


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]


def stem_tokens(tokens):
    stemmer = SnowballStemmer("english")
    return [stemmer.stem(token) for token in tokens]


def process_and_plot(tokens, title):
    token_counts = Counter(tokens)  # count the tokens
    sorted_tokens = sorted(token_counts.items(),
                           key=lambda x: x[1], reverse=True)  # sort  in DESC
    ranks = range(1, len(sorted_tokens) + 1)
    frequencies = [count for token, count in sorted_tokens]
    plot_graph(ranks, frequencies, title)
    if title == 'Original':
        print(f"Top 20 tokens ({title}):")
        for token, count in sorted_tokens[:20]:
            print(f"{token}: {count}")
        print("\n")


def plot_graph(ranks, frequencies, title):
    # Create log-log plot
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies)
    plt.xlabel('Log Rank')
    plt.ylabel('Log Frequency')
    plt.title(f'Token Frequency vs Rank ({title})')
    plt.show()


if __name__ == '__main__':
    main()
