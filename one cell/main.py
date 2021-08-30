from fpdf import FPDF

# create FDPF object
# Layout ('P', 'L') → Portrait and Landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', Custom → (100, 150))
# pdf = FPDF(orientation="P", unit="mm", format="A4") → This are the default values
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination is possible ('BU')
pdf.set_font('helvetica', '', 16)

# Add text
# w = width
# h = height
# txt = your text
# ln ( 0 False; 1 True - move cursor down to next line)

# pdf.cell(40, 100, 'Hello Workd', ln=True, border=True)  → positional way
pdf.cell(w=40, h=100, txt='Hello Workd', ln=True, border=True)
pdf.cell(40, 10, 'Good Bye World')
pdf.output('mypdf.pdf')

