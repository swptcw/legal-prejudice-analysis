from PIL import Image, ImageDraw, ImageFont
import os

# Ensure features directory exists
os.makedirs('assets/features', exist_ok=True)

# Function to create a feature image
def create_feature_image(filename, title, color, icon_type):
    width, height = 400, 200
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)
    
    # Draw title
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()
    
    text_width = len(title) * 12  # Approximate width
    text_x = (width - text_width) // 2
    draw.text((text_x, 20), title, fill=(255, 255, 255), font=font)
    
    # Draw icon based on type
    if icon_type == "framework":
        # Draw a document with sections
        doc_x, doc_y = width//2 - 30, height//2 - 20
        doc_width, doc_height = 60, 80
        draw.rectangle([(doc_x, doc_y), (doc_x + doc_width, doc_y + doc_height)], fill=(255, 255, 255))
        
        # Draw lines representing text
        for i in range(5):
            line_y = doc_y + 15 + i * 12
            draw.line([(doc_x + 10, line_y), (doc_x + doc_width - 10, line_y)], fill=color, width=2)
    
    elif icon_type == "risk":
        # Draw a risk matrix
        matrix_x, matrix_y = width//2 - 40, height//2 - 30
        matrix_size = 80
        draw.rectangle([(matrix_x, matrix_y), (matrix_x + matrix_size, matrix_y + matrix_size)], outline=(255, 255, 255), width=2)
        
        # Draw grid lines
        for i in range(1, 4):
            # Horizontal lines
            draw.line([(matrix_x, matrix_y + i * matrix_size//4), 
                      (matrix_x + matrix_size, matrix_y + i * matrix_size//4)], 
                      fill=(255, 255, 255), width=1)
            
            # Vertical lines
            draw.line([(matrix_x + i * matrix_size//4, matrix_y), 
                      (matrix_x + i * matrix_size//4, matrix_y + matrix_size)], 
                      fill=(255, 255, 255), width=1)
        
        # Draw a risk point
        draw.ellipse([(matrix_x + 60, matrix_y + 15), (matrix_x + 70, matrix_y + 25)], fill=(231, 76, 60))
    
    elif icon_type == "guide":
        # Draw a checklist
        check_x, check_y = width//2 - 30, height//2 - 40
        check_width, check_height = 60, 80
        
        # Draw clipboard
        draw.rectangle([(check_x, check_y), (check_x + check_width, check_y + check_height)], fill=(255, 255, 255))
        draw.rectangle([(check_x + 15, check_y - 10), (check_x + 45, check_y)], fill=(200, 200, 200))
        
        # Draw checklist items
        for i in range(5):
            item_y = check_y + 15 + i * 15
            # Checkbox
            draw.rectangle([(check_x + 10, item_y), (check_x + 20, item_y + 10)], outline=(color[0], color[1], color[2]))
            # Check mark in some boxes
            if i % 2 == 0:
                draw.line([(check_x + 12, item_y + 5), (check_x + 15, item_y + 8)], fill=color, width=2)
                draw.line([(check_x + 15, item_y + 8), (check_x + 18, item_y + 2)], fill=color, width=2)
            # Line representing text
            draw.line([(check_x + 25, item_y + 5), (check_x + 50, item_y + 5)], fill=color, width=2)
    
    elif icon_type == "calculator":
        # Draw a calculator
        calc_x, calc_y = width//2 - 30, height//2 - 40
        calc_width, calc_height = 60, 80
        
        # Draw calculator body
        draw.rectangle([(calc_x, calc_y), (calc_x + calc_width, calc_y + calc_height)], fill=(50, 50, 50))
        
        # Draw calculator screen
        draw.rectangle([(calc_x + 5, calc_y + 5), (calc_x + calc_width - 5, calc_y + 20)], fill=(200, 255, 200))
        
        # Draw calculator buttons
        button_size = 10
        for row in range(4):
            for col in range(4):
                button_x = calc_x + 8 + col * (button_size + 5)
                button_y = calc_y + 30 + row * (button_size + 5)
                draw.rectangle([(button_x, button_y), (button_x + button_size, button_y + button_size)], fill=(200, 200, 200))
    
    elif icon_type == "api":
        # Draw API icon
        api_x, api_y = width//2 - 40, height//2 - 20
        
        # Draw brackets representing API
        # Left bracket
        draw.line([(api_x, api_y), (api_x + 15, api_y)], fill=(255, 255, 255), width=3)
        draw.line([(api_x, api_y), (api_x, api_y + 40)], fill=(255, 255, 255), width=3)
        draw.line([(api_x, api_y + 40), (api_x + 15, api_y + 40)], fill=(255, 255, 255), width=3)
        
        # Right bracket
        draw.line([(api_x + 65, api_y), (api_x + 80, api_y)], fill=(255, 255, 255), width=3)
        draw.line([(api_x + 80, api_y), (api_x + 80, api_y + 40)], fill=(255, 255, 255), width=3)
        draw.line([(api_x + 65, api_y + 40), (api_x + 80, api_y + 40)], fill=(255, 255, 255), width=3)
        
        # Draw "API" text
        draw.text((api_x + 25, api_y + 10), "API", fill=(255, 255, 255), font=font)
    
    elif icon_type == "case":
        # Draw a case file
        case_x, case_y = width//2 - 40, height//2 - 30
        case_width, case_height = 80, 60
        
        # Draw folder
        draw.rectangle([(case_x, case_y), (case_x + case_width, case_y + case_height)], fill=(241, 196, 15))
        draw.polygon([(case_x, case_y), (case_x + 20, case_y - 15), (case_x + 60, case_y - 15), (case_x + 80, case_y)], fill=(241, 196, 15))
        
        # Draw lines representing text
        for i in range(3):
            line_y = case_y + 15 + i * 12
            draw.line([(case_x + 10, line_y), (case_x + case_width - 10, line_y)], fill=(color[0], color[1], color[2]), width=2)
    
    # Save the image
    img.save(f'assets/features/{filename}')
    return f'assets/features/{filename}'

# Create feature images
feature_images = [
    ("feature-framework.jpg", "Legal Prejudice Framework", (52, 152, 219), "framework"),
    ("feature-risk.jpg", "Risk & Probability Analysis", (46, 204, 113), "risk"),
    ("feature-guide.jpg", "Practical Implementation", (155, 89, 182), "guide"),
    ("feature-calculator.jpg", "Interactive Risk Calculator", (52, 73, 94), "calculator"),
    ("feature-api.jpg", "API & Integration", (230, 126, 34), "api"),
    ("feature-case.jpg", "Case Studies", (231, 76, 60), "case")
]

for filename, title, color, icon_type in feature_images:
    path = create_feature_image(filename, title, color, icon_type)
    print(f"Created {path}")

print("All feature images created successfully!")