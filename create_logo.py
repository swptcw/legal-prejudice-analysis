from PIL import Image, ImageDraw, ImageFont
import os

# Create regular logo
logo_width, logo_height = 200, 50
logo = Image.new('RGBA', (logo_width, logo_height), (255, 255, 255, 0))
draw = ImageDraw.Draw(logo)

# Draw a scale of justice icon
scale_width = 30
scale_height = 30
scale_left = 10
scale_top = 10

# Draw the scale base
draw.rectangle(
    [(scale_left + scale_width//2 - 2, scale_top + scale_height - 10), 
     (scale_left + scale_width//2 + 2, scale_top + scale_height)], 
    fill=(44, 62, 80)
)

# Draw the scale arm
draw.rectangle(
    [(scale_left, scale_top + scale_height//2 - 1), 
     (scale_left + scale_width, scale_top + scale_height//2 + 1)], 
    fill=(44, 62, 80)
)

# Draw the scale dishes
draw.ellipse(
    [(scale_left, scale_top + scale_height//2 - 5), 
     (scale_left + 10, scale_top + scale_height//2 + 5)], 
    outline=(44, 62, 80), width=2
)
draw.ellipse(
    [(scale_left + scale_width - 10, scale_top + scale_height//2 - 5), 
     (scale_left + scale_width, scale_top + scale_height//2 + 5)], 
    outline=(44, 62, 80), width=2
)

# Draw text "LPA"
font_size = 24
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

draw.text((scale_left + scale_width + 10, scale_top), "LPA", fill=(44, 62, 80), font=font)

# Draw text "Legal Prejudice Analysis"
font_size = 10
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

draw.text((scale_left + scale_width + 10, scale_top + 30), "Legal Prejudice Analysis", fill=(44, 62, 80), font=font)

# Save the logo
logo.save('assets/logo.png')

# Create white version of the logo
logo_white = Image.new('RGBA', (logo_width, logo_height), (255, 255, 255, 0))
draw_white = ImageDraw.Draw(logo_white)

# Draw the scale base
draw_white.rectangle(
    [(scale_left + scale_width//2 - 2, scale_top + scale_height - 10), 
     (scale_left + scale_width//2 + 2, scale_top + scale_height)], 
    fill=(255, 255, 255)
)

# Draw the scale arm
draw_white.rectangle(
    [(scale_left, scale_top + scale_height//2 - 1), 
     (scale_left + scale_width, scale_top + scale_height//2 + 1)], 
    fill=(255, 255, 255)
)

# Draw the scale dishes
draw_white.ellipse(
    [(scale_left, scale_top + scale_height//2 - 5), 
     (scale_left + 10, scale_top + scale_height//2 + 5)], 
    outline=(255, 255, 255), width=2
)
draw_white.ellipse(
    [(scale_left + scale_width - 10, scale_top + scale_height//2 - 5), 
     (scale_left + scale_width, scale_top + scale_height//2 + 5)], 
    outline=(255, 255, 255), width=2
)

# Draw text "LPA"
font_size = 24
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

draw_white.text((scale_left + scale_width + 10, scale_top), "LPA", fill=(255, 255, 255), font=font)

# Draw text "Legal Prejudice Analysis"
font_size = 10
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

draw_white.text((scale_left + scale_width + 10, scale_top + 30), "Legal Prejudice Analysis", fill=(255, 255, 255), font=font)

# Save the white logo
logo_white.save('assets/logo-white.png')

print("Logos created successfully!")