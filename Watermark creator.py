from PIL import Image, ImageDraw, ImageFont

# Load the input image
input_image = Image.open("images.jpg")

# Define the text to be used as the watermark
text = "Watermark"

# Define the font and size for the watermark
font = ImageFont.truetype("arial.ttf", size=36)

# Get the size of the text
text_bbox = font.getbbox(text)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Calculate the position for the watermark
pos_x = input_image.width - text_width - 10
pos_y = input_image.height - text_height - 10

# Create a new ImageDraw object for the input image
draw = ImageDraw.Draw(input_image)

# Draw the text on the input image
draw.text((pos_x, pos_y), text, font=font, fill=(255, 255, 255, 128))

# Save the watermarked image
input_image.save("watermarked_image.jpg")
# Load the watermarked image
watermarked_image = Image.open("watermarked_image.jpg")

# Display the image in a window
watermarked_image.show()