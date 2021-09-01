from fpdf import FPDF

title = 'Lorem Ipsum'


class PDF(FPDF):
    # to set our custom fonts, we will have to add this fonts to our constructor
    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)
        # adding custom (google) fonts
        self.add_font('Roboto', 'B', '/home/phsw/Downloads/Roboto/Roboto-Bold.ttf', uni=True)
        self.add_font('Roboto', 'I', '/home/phsw/Downloads/Roboto/Roboto-Italic.ttf', uni=True)
        self.add_font('Roboto', '', '/home/phsw/Downloads/Roboto/Roboto-Regular.ttf', uni=True)

    def header(self):
        # font
        self.set_font('Roboto', 'B', 15)
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
        self.set_font('Roboto', 'I', 10)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')  # page_no (page number) / nb (number fs pages)

    # adding chapter title to start of each chapter.
    def chapter_title(self, ch_num, ch_title, link):
        # set location
        self.set_link(link)
        # set font
        self.set_font('Roboto', '', 12)
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
        self.multi_cell(165, 5, txt)
        # line break
        self.ln()
        # end each charpter
        self.set_font('times', 'I', 12)
        self.cell(0, 5, "End of Chapter")

    def print_chapter(self, ch_num, ch_title, name, link):
        self.add_page()
        self.chapter_title(ch_num, ch_title, link)
        self.chapter_body(name)


# pdf = FPDF('P', 'mm', 'Letter') → [ dessa forma gera erro:  __init__() takes 1 positional argument but 4 were given]
pdf = PDF(orientation="P", unit="mm", format="Letter")  # se passar como posicionais vai dar erro, pois reescrevemos o init e isso obriga a passar os parametros de forma posicional

# metadata
pdf.set_title(title)
pdf.set_author('Pedro Madureira')

# create links
django_link = 'https://docs.djangoproject.com/en/3.2/'
ch1_link = pdf.add_link()
ch2_link = pdf.add_link()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()
pdf.image('django.jpg', x=-0.5, w=pdf.w+1)

# Attach links
pdf.cell(0, 10, 'Django documentation', ln=1, link=django_link)
pdf.cell(0, 10, 'Chapter 1', ln=1, link=ch1_link)
pdf.cell(0, 10, 'Chapter 2', ln=1, link=ch2_link)

# Add chapter
pdf.print_chapter(1, 'A runaway reef', 'chp1.txt', ch1_link)
pdf.print_chapter(2, 'the rpos and cons', 'chp2.txt', ch2_link)


pdf.output('pdf_3.pdf')
