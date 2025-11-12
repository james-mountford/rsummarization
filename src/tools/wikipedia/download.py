import wikipedia
import argparse
from pathlib import Path
from conf import PROJECT_ROOT

def main():
    parser = argparse.ArgumentParser(description='Download a specified Wikipedia article as plaintext.')
    parser.add_argument('--lang', default='en', help='Language to download the article in')
    parser.add_argument('--article', required=True, help='Name of the article to download')
    parser.add_argument('--output-dir', default='samples', help='Directory to save the downloaded file')
    args = parser.parse_args()

    try:
        # Target the right Wikipedia article in the correct language and fetch content
        wikipedia.set_lang(args.lang)
        target_article = wikipedia.page(args.article, auto_suggest=False, redirect=False)
        article_text = target_article.content

        # Ensure sample dir exists or create if not; resolve from project root
        target_dir = PROJECT_ROOT / 'data' / 'examples' / 'wikipedia'
        target_dir.mkdir(parents=True, exist_ok=True)

        # Standardize saved file names and construct the path
        file_name = args.article.lower().replace(' ', '_') + '.txt'
        target_file = target_dir / file_name

        # Open target file and write the article contents
        with open(target_file, 'w', encoding='utf-8') as output:
            output.write(article_text)
    
        print(f'Successfully downloaded Wikipedia article "{args.article}" to target file "{target_file}"')

    except Exception as error:
        print(f'Error attempting to download Wikipedia article "{args.article}". Error: {error}')

if __name__ == '__main__':
    main()