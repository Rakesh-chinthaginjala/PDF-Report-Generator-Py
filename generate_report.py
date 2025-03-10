import pandas as pd
from fpdf import FPDF


# Sample data file (data.csv) should exist in the same directory
# Columns: Name, Age, Score

def read_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def analyze_data(df):
    summary = {
        "Total Entries": len(df),
        "Average Age": df["Age"].mean(),
        "Average Score": df["Score"].mean(),
        "Highest Score": df["Score"].max(),
        "Lowest Score": df["Score"].min()
    }
    return summary


def generate_pdf_report(summary, output_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Data Analysis Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for key, value in summary.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)

    pdf.output(output_filename)
    print(f"Report saved as {output_filename}")


if __name__ == "__main__":
    filename = "data.csv"  # Ensure this file exists
    df = read_data(filename)
    if df is not None:
        summary = analyze_data(df)
        generate_pdf_report(summary, "report.pdf")
