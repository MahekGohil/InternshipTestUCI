import streamlit as st
import fitz  # PyMuPDF
import json
from io import BytesIO

st.set_page_config(page_title="PDF Compliance Analyzer", layout="wide")
st.title(" PDF Compliance Analyzer")

st.markdown("""
Upload a proposal document in PDF format.  
The tool will check:
- **Technical Requirements** ≤ 8 pages  
- **Budget** ≤ 4 pages  
- **Qualification** ≤ 4 pages  
""")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if not uploaded_file:
    st.info("Please upload a PDF to start.")
else:
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    except Exception:
        st.error("Invalid PDF file.")
        st.stop()

    with st.sidebar:
        st.header("File Info")
        st.write(f"**File:** {uploaded_file.name}")
        st.write(f"**Pages:** {doc.page_count}")

    # Preview first page
    pix = doc[0].get_pixmap()
    img_bytes = BytesIO(pix.tobytes("png"))
    st.image(img_bytes, caption="First Page Preview", use_container_width=True)

    # Section rules
    sections = {
        "Technical Requirements": {"max_pages": 8, "pages_found": 0},
        "Budget": {"max_pages": 4, "pages_found": 0},
        "Qualification": {"max_pages": 4, "pages_found": 0},
    }

   
    for page in doc:
        text = page.get_text().lower()
        for sec in sections:
            if sec.lower() in text:
                sections[sec]["pages_found"] += 1

  
    results = []
    for sec, data in sections.items():
        status = " Pass" if 0 < data["pages_found"] <= data["max_pages"] else "❌ Fail"
        results.append({
            "Section": sec,
            "Pages Found": data["pages_found"],
            "Allowed Pages": data["max_pages"],
            "Status": status
        })

    st.subheader("Compliance Results")
    st.table(results)

    # JSON output
    report = {
        "format": {"file_type": "pass"},
        "content": {
            sec: {
                "pages_found": data["pages_found"],
                "allowed_pages": data["max_pages"],
                "status": "pass" if "" in status else "fail"
            }
            for sec, data, status in zip(sections.keys(), sections.values(), [r["Status"] for r in results])
        }
    }

    st.download_button(
        "Download JSON Report",
        data=json.dumps(report, indent=2),
        file_name="compliance_report.json",
        mime="application/json"
    )
