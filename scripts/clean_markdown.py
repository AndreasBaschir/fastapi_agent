import re
import sys
import json

def clean_markdown_for_json(file_path: str) -> str:
    """
    Reads a Markdown file and converts its content into a single-line,
    plain text string suitable for embedding in a JSON payload.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # 1. Remove Markdown tables by removing lines with pipe characters
        lines = text.split('\n')
        lines = [line for line in lines if '|' not in line]
        text = '\n'.join(lines)

        # 2. Remove Markdown headings, list markers, blockquotes, and horizontal rules
        text = re.sub(r'^(#+\s*|\*\s*|-\s*|>\s*|---|===)', '', text, flags=re.MULTILINE)

        # 3. Remove image tags like ![alt](src)
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)

        # 4. Remove link tags like [text](url), keeping the text
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)

        # 5. Remove bold/italic markers like **, *, __, _
        text = re.sub(r'(\*\*|__|\*|_)', '', text)

        # 6. Replace all newline, tab, and multiple spaces with a single space
        text = re.sub(r'[\s\t\n\r]+', ' ', text)

        # 7. Remove leading/trailing whitespace
        text = text.strip()

        # 8. NEW: Use json.dumps() to perfectly escape the string for JSON
        # Then remove the surrounding quotes that json.dumps() adds
        escaped_text = json.dumps(text)[1:-1]
        
        return escaped_text

    except FileNotFoundError:
        return f"Error: File not found at '{file_path}'"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts.clean_markdown.py <path_to_markdown_file>")
    else:
        input_file = sys.argv[1]
        cleaned_text = clean_markdown_for_json(input_file)
        print(cleaned_text, end='')  # end='' prevents the trailing newline