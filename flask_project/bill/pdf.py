from fpdf import FPDF

class mypdf(FPDF):
    cursor = 0;
    font_size = 16;
    total = 0;
    def write(self,bill, folder_name):
        self.add_page();
        self.set_font("helvetica", "B", 16);
        self.cell(70, self.font_size, "product", 1);
        self.cell(35, self.font_size, "Quantaty", 1);
        self.cell(35, self.font_size, "Price", 1);
        self.cell(50, self.font_size, "Amount", 1);
        self.ln(self.font_size);
        for row in bill:
            self.cell(70, self.font_size, row["item"], 1);
            self.cell(35, self.font_size, row["quntaty"], 1);
            self.cell(35, self.font_size, row["price"], 1);
            self.cell(50, self.font_size, row["amount"], 1);
            self.total += int(row["amount"]);
            self.ln(self.font_size);

        self.cell(140, self.font_size, "TOTAL = ", 1);
        self.cell(50, self.font_size, str(self.total), 1);
        self.output(f"./database/" + folder_name + "/bill.pdf");
		
