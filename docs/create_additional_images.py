from PIL import Image, ImageDraw, ImageFont
import os

# Create documentation image
def create_documentation_image():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), (245, 245, 245))
    draw = ImageDraw.Draw(img)
    
    # Draw sidebar
    sidebar_width = 150
    draw.rectangle([(0, 0), (sidebar_width, height)], fill=(52, 73, 94))
    
    # Draw sidebar items
    sidebar_items = [
        "Framework",
        "Risk Analysis",
        "Implementation",
        "Case Studies",
        "API Reference",
        "Integration"
    ]
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 18)
        sidebar_font = ImageFont.truetype("arial.ttf", 12)
        content_font = ImageFont.truetype("arial.ttf", 14)
        content_small_font = ImageFont.truetype("arial.ttf", 10)
    except IOError:
        title_font = ImageFont.load_default()
        sidebar_font = ImageFont.load_default()
        content_font = ImageFont.load_default()
        content_small_font = ImageFont.load_default()
    
    # Draw sidebar title
    draw.text((20, 30), "Documentation", fill=(255, 255, 255), font=title_font)
    
    # Draw sidebar items
    for i, item in enumerate(sidebar_items):
        y = 80 + i * 40
        # Highlight the first item
        if i == 0:
            draw.rectangle([(0, y-5), (sidebar_width, y+25)], fill=(41, 128, 185))
        draw.text((20, y), item, fill=(255, 255, 255), font=sidebar_font)
    
    # Draw main content area
    # Header
    draw.rectangle([(sidebar_width, 0), (width, 60)], fill=(236, 240, 241))
    draw.text((sidebar_width + 20, 20), "Legal Prejudice Analysis Framework", fill=(52, 73, 94), font=title_font)
    
    # Content
    content_x = sidebar_width + 20
    content_y = 80
    
    # Section title
    draw.text((content_x, content_y), "1. Introduction to Legal Prejudice", fill=(52, 73, 94), font=content_font)
    content_y += 30
    
    # Content paragraphs
    paragraphs = [
        "Legal prejudice refers to bias or preconceived judgment that may affect judicial decision-making. This framework provides a structured approach to identifying, analyzing, and responding to potential prejudice in legal proceedings.",
        
        "The framework is based on statutory provisions (28 U.S.C. §§ 455, 144) and key Supreme Court precedents including Liteky v. United States and Caperton v. A.T. Massey Coal Co."
    ]
    
    for paragraph in paragraphs:
        # Wrap text to fit width
        words = paragraph.split()
        line = ""
        y_offset = 0
        for word in words:
            test_line = line + word + " "
            # Check if adding this word would exceed the width
            if content_font.getbbox(test_line)[2] < (width - content_x - 20):
                line = test_line
            else:
                draw.text((content_x, content_y + y_offset), line, fill=(0, 0, 0), font=content_small_font)
                y_offset += 20
                line = word + " "
        
        # Draw the last line
        if line:
            draw.text((content_x, content_y + y_offset), line, fill=(0, 0, 0), font=content_small_font)
        
        content_y += y_offset + 30
    
    # Draw a table
    table_y = content_y
    draw.rectangle([(content_x, table_y), (width - 20, table_y + 30)], fill=(52, 73, 94))
    draw.text((content_x + 10, table_y + 8), "Prejudice Type", fill=(255, 255, 255), font=content_small_font)
    draw.text((content_x + 150, table_y + 8), "Risk Level", fill=(255, 255, 255), font=content_small_font)
    draw.text((content_x + 250, table_y + 8), "Response", fill=(255, 255, 255), font=content_small_font)
    
    # Table rows
    row_data = [
        ("Relationship-based", "High", "Motion to Recuse"),
        ("Conduct-based", "Medium", "Document & Monitor"),
        ("Contextual", "Low", "Standard Disclosure")
    ]
    
    for i, (type_text, risk, response) in enumerate(row_data):
        row_y = table_y + 30 + i * 30
        # Alternating row colors
        if i % 2 == 0:
            draw.rectangle([(content_x, row_y), (width - 20, row_y + 30)], fill=(236, 240, 241))
        else:
            draw.rectangle([(content_x, row_y), (width - 20, row_y + 30)], fill=(245, 245, 245))
        
        draw.text((content_x + 10, row_y + 8), type_text, fill=(0, 0, 0), font=content_small_font)
        draw.text((content_x + 150, row_y + 8), risk, fill=(0, 0, 0), font=content_small_font)
        draw.text((content_x + 250, row_y + 8), response, fill=(0, 0, 0), font=content_small_font)
    
    # Save the image
    img.save('assets/documentation.png')
    print("Documentation image created successfully!")

# Create demo preview image
def create_demo_preview():
    width, height = 500, 350
    img = Image.new('RGB', (width, height), (245, 245, 245))
    draw = ImageDraw.Draw(img)
    
    # Draw header
    draw.rectangle([(0, 0), (width, 50)], fill=(52, 73, 94))
    
    try:
        header_font = ImageFont.truetype("arial.ttf", 18)
        title_font = ImageFont.truetype("arial.ttf", 16)
        label_font = ImageFont.truetype("arial.ttf", 12)
        value_font = ImageFont.truetype("arial.ttf", 14)
    except IOError:
        header_font = ImageFont.load_default()
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        value_font = ImageFont.load_default()
    
    # Draw header text
    draw.text((20, 15), "Legal Prejudice Analysis - Risk Calculator Demo", fill=(255, 255, 255), font=header_font)
    
    # Draw tabs
    tabs = ["Relationship Factors", "Conduct Factors", "Contextual Factors", "Results"]
    tab_width = width // len(tabs)
    
    for i, tab in enumerate(tabs):
        tab_x = i * tab_width
        # Highlight the last tab
        if i == len(tabs) - 1:
            draw.rectangle([(tab_x, 50), (tab_x + tab_width, 80)], fill=(41, 128, 185))
            text_color = (255, 255, 255)
        else:
            draw.rectangle([(tab_x, 50), (tab_x + tab_width, 80)], fill=(236, 240, 241))
            text_color = (52, 73, 94)
        
        # Center the text in the tab
        text_width = label_font.getbbox(tab)[2]
        text_x = tab_x + (tab_width - text_width) // 2
        draw.text((text_x, 60), tab, fill=text_color, font=label_font)
    
    # Draw results content
    draw.text((20, 100), "Risk Assessment Results", fill=(52, 73, 94), font=title_font)
    
    # Draw risk score card
    card_x, card_y = 20, 140
    card_width, card_height = 150, 100
    draw.rectangle([(card_x, card_y), (card_x + card_width, card_y + card_height)], fill=(231, 76, 60))
    draw.text((card_x + 30, card_y + 10), "Risk Score", fill=(255, 255, 255), font=label_font)
    draw.text((card_x + 60, card_y + 40), "18", fill=(255, 255, 255), font=ImageFont.load_default())
    draw.text((card_x + 40, card_y + 70), "HIGH RISK", fill=(255, 255, 255), font=label_font)
    
    # Draw risk matrix
    matrix_x, matrix_y = 200, 140
    matrix_width, matrix_height = 250, 200
    draw.rectangle([(matrix_x, matrix_y), (matrix_x + matrix_width, matrix_y + matrix_height)], fill=(236, 240, 241))
    draw.text((matrix_x + 80, matrix_y + 10), "Risk Matrix", fill=(52, 73, 94), font=label_font)
    
    # Draw matrix grid
    cell_size = 40
    for i in range(6):
        # Horizontal lines
        draw.line([(matrix_x + 30, matrix_y + 40 + i*cell_size), 
                  (matrix_x + 30 + 5*cell_size, matrix_y + 40 + i*cell_size)], 
                  fill=(189, 195, 199))
        
        # Vertical lines
        draw.line([(matrix_x + 30 + i*cell_size, matrix_y + 40), 
                  (matrix_x + 30 + i*cell_size, matrix_y + 40 + 5*cell_size)], 
                  fill=(189, 195, 199))
    
    # Draw axis labels
    draw.text((matrix_x + 100, matrix_y + 25), "Likelihood", fill=(52, 73, 94), font=label_font)
    draw.text((matrix_x + 10, matrix_y + 120), "Impact", fill=(52, 73, 94), font=label_font)
    
    # Draw risk zones
    # Low risk zone (green)
    for i in range(2):
        for j in range(2):
            draw.rectangle([
                (matrix_x + 30 + i*cell_size, matrix_y + 40 + j*cell_size),
                (matrix_x + 30 + (i+1)*cell_size, matrix_y + 40 + (j+1)*cell_size)
            ], fill=(46, 204, 113, 100))
    
    # Medium risk zone (yellow)
    for i in range(2, 4):
        for j in range(2, 4):
            draw.rectangle([
                (matrix_x + 30 + i*cell_size, matrix_y + 40 + j*cell_size),
                (matrix_x + 30 + (i+1)*cell_size, matrix_y + 40 + (j+1)*cell_size)
            ], fill=(241, 196, 15, 100))
    
    # High risk zone (red)
    for i in range(3, 5):
        for j in range(3, 5):
            draw.rectangle([
                (matrix_x + 30 + i*cell_size, matrix_y + 40 + j*cell_size),
                (matrix_x + 30 + (i+1)*cell_size, matrix_y + 40 + (j+1)*cell_size)
            ], fill=(231, 76, 60, 100))
    
    # Draw risk points
    points = [(4, 4), (3, 5), (5, 3), (2, 4)]
    for x, y in points:
        point_x = matrix_x + 30 + x * cell_size - cell_size//2
        point_y = matrix_y + 40 + y * cell_size - cell_size//2
        draw.ellipse([(point_x-5, point_y-5), (point_x+5, point_y+5)], fill=(52, 73, 94))
    
    # Draw recommendations section
    rec_x, rec_y = 20, 260
    draw.text((rec_x, rec_y), "Recommended Actions:", fill=(52, 73, 94), font=title_font)
    
    recommendations = [
        "1. File motion for recusal within 48 hours",
        "2. Document all instances of potential prejudice",
        "3. Prepare alternative venue motion",
        "4. Consult with ethics counsel"
    ]
    
    for i, rec in enumerate(recommendations):
        draw.text((rec_x, rec_y + 30 + i*25), rec, fill=(0, 0, 0), font=label_font)
    
    # Save the image
    img.save('assets/demo-preview.png')
    print("Demo preview image created successfully!")

# Create integration logos
def create_integration_logos():
    # Create directory for logos
    os.makedirs('assets', exist_ok=True)
    
    # Function to create a simple logo
    def create_logo(filename, text, color):
        width, height = 120, 60
        img = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw colored rectangle
        draw.rectangle([(10, 10), (width-10, height-10)], fill=color)
        
        # Draw text
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            font = ImageFont.load_default()
        
        text_width = font.getbbox(text)[2]
        text_x = (width - text_width) // 2
        draw.text((text_x, 20), text, fill=(255, 255, 255), font=font)
        
        # Save the logo
        img.save(f'assets/logo-{filename}.png')
        return f'assets/logo-{filename}.png'
    
    # Create logos for different integrations
    integrations = [
        ("clio", "Clio", (41, 128, 185)),
        ("practice-panther", "Practice Panther", (46, 204, 113)),
        ("mycase", "MyCase", (155, 89, 182)),
        ("smokeball", "Smokeball", (230, 126, 34)),
        ("filevine", "Filevine", (231, 76, 60))
    ]
    
    for filename, text, color in integrations:
        path = create_logo(filename, text, color)
        print(f"Created {path}")

# Create all images
create_documentation_image()
create_demo_preview()
create_integration_logos()

print("All additional images created successfully!")