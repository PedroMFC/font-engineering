from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options

# Open the font
with TTFont('../fonts/Andén-Regular.otf') as font:

    """
    List Font tables
    """
    print(font.keys())

    """
    List Font name
    """
    name = font.get('name')
    for record in name.names:
        if record.nameID == 1:
            font_family_name = record.string.decode(record.getEncoding())
            print(f"Font Family Name: {font_family_name}")
            break
    """
    Change Font name
    """
    # Change font name
    for record in font['name'].names:
        if record.nameID == 1:
            record.string = "New Font Name".encode(record.getEncoding())
            break

    # Save
    # font.save('path/to/your/modified_fontfile.otf')

    """
    Subset
    """
    # subsetter configuration
    options = Options()
    subsetter = Subsetter(options=options)

    # Define characters to maintain
    subsetter.populate(text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

    # Apply subset
    subsetter.subset(font)

    # Save
    # font.save('path/to/your/subsetted_fontfile.otf')

    """
    Glyphs inspection
    """
    for glyph_name in font.glyphOrder:
        print(glyph_name)


