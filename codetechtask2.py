import pandas as_csv(StringIO(csv_data)) 
from fpdf import FPDF
from io import StringIO


csv_data = """Date,Product,Units Sold,Revenue
2025-07-01,Widget A,100,5000
2025-07-02,Widget B,150,7500
2025-07-03,Widget A,120,6000
2025-07-04,Widget C,90,4500
2025-07-05,Widget B,130,6500
"""

df = pd.read
# Analysis
total_units = df["Units Sold"].sum()
total_revenue = df["Revenue"].sum()
avg_revenue = df["Revenue"].mean()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

# PDF Report Class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Sales Report", ln=1, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=1)
        self.ln(2)

    def section_body(self, text):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, text)
        self.ln()

# Create and fill the PDF
pdf = PDF()
pdf.add_page()

pdf.section_title("Summary Statistics")
pdf.section_body(
    f"Total Units Sold: {total_units}\n"
    f"Total Revenue: ${total_revenue:,.2f}\n"
    f"Average Revenue per Day: ${avg_revenue:,.2f}\n"
    f"Top-Selling Product: {top_product}"
)

pdf.section_title("Daily Sales Records")
for idx, row in df.iterrows():
    pdf.section_body(
        f"{row['Date']} - {row['Product']} | Units Sold: {row['Units Sold']} | Revenue: ${row['Revenue']}"
    )

# Save PDF
pdf.output("sales_report_embedded.pdf")
print("PDF report generated: sales_report_embedded.pdf")
