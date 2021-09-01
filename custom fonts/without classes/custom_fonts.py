from fpdf import FPDF

# create FDPF object
# Layout ('P', 'L') → Portrait and Landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', Custom → (100, 150))
# pdf = FPDF(orientation="P", unit="mm", format="Letter")
pdf = FPDF('P', 'mm', 'Letter')

pdf.add_font('Allison', '', '/home/phsw/Downloads/Allison/Allison-Regular.ttf', uni=True)
pdf.add_font('Roboto', 'B', '/home/phsw/Downloads/Roboto/Roboto-Bold.ttf', uni=True)

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination is possible ('BU')
pdf.set_font('Allison', '', 28)

# Add text
# w = width
# h = height
# txt = your text
# ln ( 0 False; 1 True - move cursor down to next line)

# pdf.cell(40, 100, 'Hello Workd', ln=True, border=True)  → positional way
pdf.cell(w=40, h=100, txt='Hello Workd', ln=True, border=True)

pdf.set_font('roboto', 'B', 16)
pdf.cell(40, 10, 'Good Bye World')
pdf.output('mypdf.pdf')

