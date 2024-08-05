from fontTools.ttLib import TTFont

# Abre la fuente
font = TTFont('../fonts/Andén-Regular.otf')

# List font tables
print(font.keys())


# Retrieve font name
name = font['name']
for record in name.names:
    if record.nameID == 1:
        font_family_name = record.string.decode(record.getEncoding())
        print(f"Font Family Name: {font_family_name}")