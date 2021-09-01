from fpdf import FPDF


# create FDPF object
# Layout ('P', 'L') → Portrait and Landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', Custom → (100, 150))
# pdf = FPDF(orientation="P", unit="mm", format="A4") → This are the default values


class PDF(FPDF):
    def header(self):
        # logo
        self.image('ph-solucoes-logo-preto-bg-pequeno.png', 10, 8,
                   25)  # image-name, x-axis(10), y-axis(8), image-width(25), image-height(auto)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', border=True, ln=1, align='C')  # align → center
        # line break
        self.ln(20)

    # Page footer

    def footer(self):
        # set position of the footer
        self.set_y(-15)  # will start 15 mm from the bottom. If its positive, would start at the top.
        # set font
        self.set_font('helvetica', 'I', 10)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')  # page_no (page number) / nb (number fs pages)

# create PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()
# Add a page
pdf.add_page()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination is possible ('BU')
pdf.set_font('helvetica', 'BIU', 16)
pdf.set_text_color(220, 50, 50)

# Add text
# w = width
# h = height
# txt = your text
# ln ( 0 False; 1 True - move cursor down to next line)

# pdf.cell(40, 100, 'Hello Workd', ln=True, border=True)  → positional way
for i in range(1, 41):
    pdf.cell(0, 10, f'This is line {i}.', ln=True)  # width zero is full width
pdf.output('pdf_2.pdf')
