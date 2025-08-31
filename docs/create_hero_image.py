from PIL import Image, ImageDraw, ImageFont
import os
import random

# Create a hero image showing a dashboard
width, height = 800, 500
hero = Image.new('RGB', (width, height), (52, 73, 94))  # Dark blue background
draw = ImageDraw.Draw(hero)

# Draw header area
draw.rectangle([(0, 0), (width, 60)], fill=(44, 62, 80))

# Draw logo placeholder in header
draw.rectangle([(20, 15), (120, 45)], fill=(41, 128, 185))
draw.text((30, 20), "LPA", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw navigation items
nav_items = ["Dashboard", "Cases", "Analysis", "Reports", "Settings"]
nav_start = 150
for item in nav_items:
    item_width = len(item) * 8
    draw.text((nav_start, 25), item, fill=(255, 255, 255), font=ImageFont.load_default())
    nav_start += item_width + 20

# Draw sidebar
sidebar_width = 200
draw.rectangle([(0, 60), (sidebar_width, height)], fill=(41, 58, 74))

# Draw sidebar menu items
menu_items = ["Home", "Risk Assessment", "Prejudice Factors", "Documentation", "Reports", "Settings", "Help"]
menu_start = 100
for item in menu_items:
    draw.text((20, menu_start), item, fill=(236, 240, 241), font=ImageFont.load_default())
    menu_start += 40

# Draw main content area title
draw.text((sidebar_width + 20, 80), "Legal Prejudice Risk Assessment Dashboard", fill=(236, 240, 241), font=ImageFont.load_default())

# Draw risk score card
card_width, card_height = 200, 120
card_x, card_y = sidebar_width + 20, 120
draw.rectangle([(card_x, card_y), (card_x + card_width, card_y + card_height)], fill=(41, 128, 185))
draw.text((card_x + 20, card_y + 20), "Overall Risk Score", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((card_x + 70, card_y + 50), "18", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((card_x + 50, card_y + 80), "HIGH RISK", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw factor analysis card
card_x = sidebar_width + 240
draw.rectangle([(card_x, card_y), (card_x + card_width, card_y + card_height)], fill=(46, 204, 113))
draw.text((card_x + 20, card_y + 20), "Factors Analyzed", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((card_x + 80, card_y + 50), "12", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((card_x + 40, card_y + 80), "4 Critical Factors", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw recommendation card
card_x = sidebar_width + 460
draw.rectangle([(card_x, card_y), (card_x + card_width, card_y + card_height)], fill=(231, 76, 60))
draw.text((card_x + 20, card_y + 20), "Recommended Action", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((card_x + 30, card_y + 50), "File Motion", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((card_x + 20, card_y + 80), "Immediate Response", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw risk matrix
matrix_width, matrix_height = 300, 200
matrix_x, matrix_y = sidebar_width + 20, 260
draw.rectangle([(matrix_x, matrix_y), (matrix_x + matrix_width, matrix_y + matrix_height)], fill=(41, 58, 74))
draw.text((matrix_x + 100, matrix_y + 10), "Risk Matrix", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw matrix grid
cell_size = 50
for i in range(6):
    # Horizontal lines
    draw.line([(matrix_x + 50, matrix_y + 50 + i*cell_size), 
               (matrix_x + 50 + 5*cell_size, matrix_y + 50 + i*cell_size)], 
              fill=(189, 195, 199))
    
    # Vertical lines
    draw.line([(matrix_x + 50 + i*cell_size, matrix_y + 50), 
               (matrix_x + 50 + i*cell_size, matrix_y + 50 + 5*cell_size)], 
              fill=(189, 195, 199))

# Draw axis labels
draw.text((matrix_x + 150, matrix_y + 30), "Likelihood", fill=(255, 255, 255), font=ImageFont.load_default())
draw.text((matrix_x + 20, matrix_y + 150), "Impact", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw some risk points on the matrix
for _ in range(8):
    x = matrix_x + 50 + random.randint(0, 4) * cell_size + random.randint(5, cell_size-5)
    y = matrix_y + 50 + random.randint(0, 4) * cell_size + random.randint(5, cell_size-5)
    color = (231, 76, 60) if random.random() > 0.5 else (241, 196, 15)
    draw.ellipse([(x-5, y-5), (x+5, y+5)], fill=color)

# Draw factor list
list_x, list_y = sidebar_width + 340, 260
draw.rectangle([(list_x, list_y), (list_x + 320, list_y + matrix_height)], fill=(41, 58, 74))
draw.text((list_x + 80, list_y + 10), "Critical Factors", fill=(255, 255, 255), font=ImageFont.load_default())

# Draw factor items
factors = [
    "Prior representation of party",
    "Financial interest in outcome",
    "Public statements on case",
    "Personal relationship with party"
]

factor_y = list_y + 50
for factor in factors:
    draw.ellipse([(list_x + 20, factor_y-5), (list_x + 30, factor_y+5)], fill=(231, 76, 60))
    draw.text((list_x + 40, factor_y), factor, fill=(255, 255, 255), font=ImageFont.load_default())
    factor_y += 30

# Save the hero image
hero.save('assets/hero-image.png')
print("Hero image created successfully!")