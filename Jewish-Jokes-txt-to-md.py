import re

with open('Jewish-Jokes.txt', 'r', encoding='utf-8') as r:
    # Iterate through each line in the file
    content = ""
    for line in r:
        # The 'line' variable includes the trailing newline character (\n)
        # Use line.strip() to remove leading/trailing whitespace, including newlines
        processed_line = line.strip()
        
        if processed_line.startswith("(#64)"):
            continue
        
        if processed_line.startswith("(#68)"):
            continue
        
        if processed_line.startswith("Please note that there are no jokes for these numbers!"):
            continue
        
        if processed_line.startswith("(#72)"):
            continue
        
        if processed_line.startswith("No joke allocated"):
            continue
        
        if processed_line.startswith("(#385)"):
            continue
        
        if processed_line.startswith("(#1391)"):
            continue
        
        if processed_line.startswith("(#417)"):
            continue
        
        # Perform operations on the line (e.g., print it)
        content += processed_line + "\n\n"
       
    with open('Jewish-Jokes-processed.txt', 'w', encoding='utf-8') as w:
        w.write(content)

# Read the original file
with open('Jewish-Jokes-processed.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace \n with actual newlines
content = content.replace('\\n', '\n')

# Find and replace section titles with markdown format
# Pattern matches: (#1), (#820), (#2349), (XXX#000), (#C060), (#C001), etc.
pattern = r'\(([^)]*#[^)]*)\)'
content = re.sub(pattern, r'---\n\n### \1', content)

# Remove the separator before the first section
content = content.lstrip('---\n\n')

# Add main title at the beginning
markdown_content = '# Jewish Jokes\n\n' + content

# Save to markdown file
with open('Jewish-Jokes.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("Conversion complete! File saved as Jewish-Jokes.md")