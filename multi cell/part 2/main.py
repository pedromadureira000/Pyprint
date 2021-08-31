from fpdf import FPDF

title = 'Lorem Ipsum'


# create FDPF object
# Layout ('P', 'L') → Portrait and Landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', Custom → (100, 150))
# pdf = FPDF(orientation="P", unit="mm", format="A4") → This are the default values


class PDF(FPDF):
    def header(self):
        # font
        self.set_font('helvetica', 'B', 15)
        # calculate the width of title
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)  # isso vai centralizar o header ( o /2 que faz isso)
        # colors os frame, background, and text
        self.set_draw_color(0, 80, 180)  # border = blue
        self.set_fill_color(230, 230, 0)  # background → yellow
        self.set_text_color(220, 50, 50)  # text → red
        # thickness of frame (border)
        self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)  # align → center
        # line break
        self.ln(10)

    # Page footer

    def footer(self):
        # set position of the footer
        self.set_y(-15)  # will start 15 mm from the bottom. If its positive, would start at the top.
        # set font
        self.set_font('helvetica', 'I', 10)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')  # page_no (page number) / nb (number fs pages)

    # adding chapter title to start of each chapter.
    def chapter_title(self, ch_num, ch_title):
        # set font
        self.set_font('helvetica', '', 12)
        # set fill color
        self.set_fill_color(200, 220, 255)
        # chapter title
        chapter_title = f'Chapter {ch_num} : {ch_title}'
        self.cell(0, 5, chapter_title, ln=1, fill=1)

    def chapter_body(self, name):
        # read text file;
        with open(name, 'rb') as fh:  # 'rb' means that it will read text file as binary.
            txt = fh.read().decode('latin-1')
        # set font
        self.set_font('times', '', 12)
        # insert text
        self.multi_cell(0, 5, txt)
        # line break
        self.ln()
        # end each charpter
        self.set_font('times', 'I', 12)
        self.cell(0, 5, "End of Chapter")

    def print_chapter(self, ch_num, ch_title, name):
        self.add_page()
        self.chapter_title(ch_num, ch_title)
        self.chapter_body(name)


# create PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# Add chapter
pdf.print_chapter(1, 'A runaway reef', 'chp1.txt')
pdf.print_chapter(2, 'the rpos and cons', 'chp2.txt')


pdf.output('pdf_3.pdf')
# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination is possible ('BU')

# pdf.set_text_color(220, 50, 50)

# Add text
# w = width
# h = height
# txt = your text
# ln ( 0 False; 1 True - move cursor down to next line)

# pdf.cell(40, 100, 'Hello Workd', ln=True, border=True)  → positional way
