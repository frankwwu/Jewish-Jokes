import markdown
import os

def convert_md_to_pdf(input_file, output_file=None):
    """Convert a markdown file to PDF using markdown and browser print"""
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found!")
        return False
    
    # Check if it's a .md file
    if not input_file.endswith('.md'):
        print("❌ Error: Please provide a .md file!")
        return False
    
    # Generate output filename if not provided
    if output_file is None:
        output_file = input_file.replace('.md', '.html')
    elif not output_file.endswith('.html'):
        output_file += '.html'
    
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content)
        
        # Add complete HTML structure with print-friendly CSS
        html_with_style = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{os.path.basename(input_file)}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            font-size: 2em;
        }}
        h2 {{
            color: #444;
            margin-top: 25px;
            font-size: 1.5em;
        }}
        h3 {{
            color: #555;
            margin-top: 20px;
            font-size: 1.2em;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 30px 0;
        }}
        p {{
            margin: 10px 0;
        }}
        @media print {{
            body {{
                margin: 20px;
                max-width: 100%;
            }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Save HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_with_style)
        
        print(f"✓ Conversion successful!")
        print(f"  Input:  {input_file}")
        print(f"  Output: {output_file}")
        print(f"\n💡 To create PDF:")
        print(f"   1. Open {output_file} in your browser")
        print(f"   2. Press Ctrl+P (or Cmd+P on Mac)")
        print(f"   3. Select 'Save as PDF' and save")
        return True
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return False

def main():
    """Main console interface"""
    print("=" * 60)
    print("  MARKDOWN TO HTML CONVERTER")
    print("  (Print to PDF from your browser)")
    print("=" * 60)
    print()
    
    while True:
        # Get input file
        input_file = input("Enter markdown file path (or 'q' to quit): ").strip()
        
        if input_file.lower() in ['q', 'quit', 'exit']:
            print("\nGoodbye!")
            break
        
        if not input_file:
            print("❌ Please enter a file path!\n")
            continue
        
        # Remove quotes if user wrapped the path in quotes
        input_file = input_file.strip('"').strip("'")
        
        # Ask for output file (optional)
        print("\nOutput file name (press Enter for auto-generated name):")
        output_file = input("  → ").strip()
        
        if not output_file:
            output_file = None
        else:
            output_file = output_file.strip('"').strip("'")
        
        print()
        # Perform conversion
        convert_md_to_pdf(input_file, output_file)
        print()
        
        # Ask if user wants to convert another
        again = input("Convert another file? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("\nGoodbye!")
            break
        print()

if __name__ == "__main__":
    main()