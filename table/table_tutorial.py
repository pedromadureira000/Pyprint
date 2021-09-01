from fpdf import FPDF

data = (
    ("First name", "Last name", "Age", "City"),
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4  # distribute content evenly
for row in data:
    for datum in row:
        pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
    pdf.ln(line_height)
pdf.output('table_with_cells.pdf')


# from fpdf import FPDF, HTMLMixin
#
# class PDF(FPDF, HTMLMixin):
#     pass
#
# pdf = PDF()
# pdf.set_font_size(16)
# pdf.add_page()
# pdf.write_html(
#     f"""<table border="1"><thead><tr>
#     <th width="25%">{data[0][0]}</th>
#     <th width="25%">{data[0][1]}</th>
#     <th width="15%">{data[0][2]}</th>
#     <th width="35%">{data[0][3]}</th>
# </tr></thead><tbody><tr>
#     <td>{'</td><td>'.join(data[1])}</td>
# </tr><tr>
#     <td>{'</td><td>'.join(data[2])}</td>
# </tr><tr>
#     <td>{'</td><td>'.join(data[3])}</td>
# </tr><tr>
#     <td>{'</td><td>'.join(data[4])}</td>
# </tr></tbody></table>""",
#     table_line_separators=True,
# )
# pdf.output('table_html.pdf')