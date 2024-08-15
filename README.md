Text Processing with NLTK

This project is a Python-based text processing tool that reads a text file, processes the text to explore word count occurrences, and generates visualizations like word clouds. It utilizes the Natural Language Toolkit (NLTK) and other libraries to perform tokenization, stopword removal, stemming, and part-of-speech tagging.
Features

    Tokenization: Splits the text into individual words and sentences.
    Stopword Removal: Filters out common words that carry less meaning (e.g., "the", "and").
    Stemming: Reduces words to their root forms.
    Part-of-Speech Tagging: Identifies proper nouns in the text.
    Word Clouds: Generates word clouds for visualizing word frequencies.
    Repeated Word Detection: Finds repeated words in sentences.

Installation

    Clone the Repository:

    bash

git clone https://github.com/nisod/Processing-with-NLTK.git
cd text-processing-nltk

Install Dependencies:
Use pip to install the required Python packages.

bash

    pip install -r requirements.txt

    Ensure you have the following dependencies:
        nltk
        click
        matplotlib
        wordcloud

    Download NLTK Resources:
    The script automatically downloads the necessary NLTK resources.

Usage

    Running the Script:
    The script can be run from the command line. By default, it processes a file named sherlock_holmes.txt. You can specify a different file using the --file option.

    bash

    python main.py --file your_text_file.txt

    Example Output:
        Displays token frequency information.
        Generates and saves word clouds for original text, text without stopwords, stemmed text, and proper nouns.

Project Structure

    main.py: The main script for text processing.
    requirements.txt: List of dependencies.
    README.md: Project documentation.

License

This project is licensed under the MIT License.
Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
Contact

For any questions or suggestions, feel free to contact me at [daniel.nisnevich@mail.huji.ac.il].
