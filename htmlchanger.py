import re

def convert_to_django_static(html_content):
    """
    Convert regular static file references to Django static template tags.
    
    Args:
        html_content (str): The HTML content to convert
        
    Returns:
        str: Converted HTML content with Django static tags
    """
    # Patterns to match different types of static references
    patterns = [
        # src="..." pattern
        (r'src="([^"]*?)(images|js|css|fonts)/([^"]*)"', r'src="{% static \2/\3 %}"'),
        
        # href="..." pattern
        (r'href="([^"]*?)(images|js|css|fonts)/([^"]*)"', r'href="{% static \2/\3 %}"'),
        
        # url(...) pattern in style attributes
        (r'url\(([^)]*?)(images|js|css|fonts)/([^)]*)\)', r'url({% static \2/\3 %})')
    ]
    
    # Add {% load static %} at the beginning of the file if not present
    if "{% load static %}" not in html_content:
        html_content = "{% load static %}\n" + html_content
    
    # Apply each pattern
    converted_content = html_content
    for pattern, replacement in patterns:
        converted_content = re.sub(pattern, replacement, converted_content)
    
    # Add single quotes around the static paths and clean up spaces
    converted_content = re.sub(r'{%\s*static\s+([^%}]+)\s*%}', lambda m: "{% static '" + m.group(1).strip() + "' %}", converted_content)
    
    return converted_content

def convert_file(input_file_path, output_file_path):
    """
    Convert an HTML file's static references to Django static template tags.
    
    Args:
        input_file_path (str): Path to the input HTML file
        output_file_path (str): Path where the converted file will be saved
    """
    try:
        # Read the input file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Convert the content
        converted_content = convert_to_django_static(content)
        
        # Write the converted content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(converted_content)
            
        print(f"Successfully converted {input_file_path} to {output_file_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_file = "template.html"  # Replace with your input file path
    output_file = "converted_template.html"  # Replace with your desired output file path
    convert_file(input_file, output_file)

if __name__ == "__main__":

    input_file = "/home/dinesh/Desktop/Ecommerce/shipIndia/templates/home_.html"  # Change this to your input HTML file
    output_file = "/home/dinesh/Desktop/Ecommerce/shipIndia/templates/homechanged.html"  # Change this to your desired output file

    convert_file(input_file, output_file)



