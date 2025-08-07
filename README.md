# InternshipTestUCI

# AI Developer Intern Technical Assignment

**Total Time Allotted: 2 Hours**  
**This test contains 3 parts. Please read carefully.**

---

## Part 1: EDA Task (Compulsory)

### Dataset Links:
- [Retail Store Sales (Dirty) - Kaggle](https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning)
- [NYC Taxi Trip Records (Recommended - Parquet)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### What You Need To Do:
1. **Download** any one of the datasets.
2. Perform **EDA** (Exploratory Data Analysis):
   - Clean the dataset (handle missing values, fix formats, correct invalid entries).
   - Visualize the key patterns and relationships (`matplotlib`, `seaborn`, or `plotly`).
   - Explain the reasoning behind choosing each library or technique.
3. Submit as a Jupyter Notebook (`.ipynb`) or `.py` script.

---

## Part 2: Choose Any One (from Below)

### 1. Markdown Documentation Generator
**Question:**  
Suppose you have a Python codebase and you want to generate markdown documentation for each function using an LLM. Outline the steps and tools you would use.  
**Skill tested:**  
- Prompt design  
- Documentation automation  
- Integration planning

---

### 2. Social Media Content Generator
**Question:**  
How would you design a system that takes a blog article and uses an LLM to create 5 platform-specific social media posts (Twitter, LinkedIn, Instagram captions, etc.)?  
**Skill tested:**  
- Output formatting  
- Multi-prompt workflows  
- Content adaptation

---

### 3. Website/POC Generator Flow
**Question:**  
You need to build a flow where a user gives a one-line business idea and the system generates a basic website scaffold using LLM + templating. Explain the architecture and where you'd use AI vs traditional code.  
**Skill tested:**  
- AI system design thinking  
- Architectural reasoning

---

### 4. Prompt Chaining for Content Creation
**Question:**  
Given a requirement to create both a product title and a meta description from the same input CSV row, how would you design the prompts so that both outputs are coherent and optimized for SEO?  
**Skill tested:**  
- Prompt engineering  
- LLM output consistency

---

## Part 3: PDF Compliance Analyzer (Compulsory)

### Task: PDF Compliance Analyzer

### Objective:
Design and implement a document analyzer that validates uploaded PDF files against a set of predefined formatting and content rules.

### Background:
Organizations often receive proposal documents in PDF format that must adhere to strict formatting guidelines. This task simulates an internal tool designed to verify these rules automatically.

### Requirements:

#### A. File Format Validation:
- Uploaded file must be in `.pdf` format.
- Reject any file that is not a valid PDF.

#### B. Formatting Validation (OCR or metadata-based):
- Font Size must be exactly **12 px**.
- Font Family must be **Times New Roman**.
- Margin on all sides must be **1 inch**.
- Use PDF parsers (like `pdfplumber`, `PyMuPDF`, `pdfminer.six`) or OCR tools (`Tesseract`) depending on file type.

#### C. Content Section Validation:
- Ensure the following sections exist and are within the allowed page limits:

| Section Name           | Max Pages |
|------------------------|-----------|
| Technical Requirements | 8 pages   |
| Budget                 | 4 pages   |
| Qualification          | 4 pages   |

- Detect sections using keywords or LLMs (optional).
- Count the number of pages each section spans.
- Flag sections that exceed the limits.

#### D. Output:
Generate a JSON or plain text report summarizing the validation results.

**Example Output:**
```json
{
  "format": {
    "file_type": "pass",
    "font_size": "fail",
    "font_family": "pass",
    "margin": "pass"
  },
  "content": {
    "technical_requirements_pages": 9,
    "technical_requirements": "fail",
    "budget_pages": 3,
    "budget": "pass",
    "qualification_pages": 4,
    "qualification": "pass"
  }
}
```

### Constraints

- Use **Python**.
- **Recommended libraries**: `pdfminer.six`, `PyMuPDF (fitz)`, `pdfplumber`, `PyPDF2`, `pytesseract`.
- **Optional**: Use an LLM (e.g., OpenAI, Cohere, or local models) for fuzzy section detection.

---

### Bonus (Optional Enhancements)

- Minimal web interface using **Streamlit** or **FastAPI** for file upload.
- Option to **download the compliance report**.
- Highlight **violations on document pages** (annotated view).

---

### Submission Guidelines

- Provide **complete source code** with setup instructions.
- Include a **sample PDF** with known formatting violations.
- Add a **README** with:
  - Tool usage instructions  
  - Any assumptions made

---

### Submission Structure

#### Folder Naming and Structure

Create a main folder with your **full name**.

Inside it, include:

- `EDA/` → for Part 1  
- `Q1/`, `Q2/`, etc. → only for the selected question from Part 2  
- `PDFAnalyzer/` → for Part 3

#### Example:
```
Aditya/
├── EDA/
│   └── nyc_taxi_eda.ipynb
├── Q3/
│   └── website_skeleton_architecture.md
├── PDFAnalyzer/
│   ├── pdf_checker.py
│   ├── sample_invalid.pdf
│   └── README.md
└── README.md
```

---

### How to Submit

- **Zip the main folder** (e.g., `Aditya.zip`)  
- Upload it via the **portal/form** shared with you.

---

If you face any issue during the test, please reach out to the coordinator immediately.
