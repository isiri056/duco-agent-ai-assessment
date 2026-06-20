# DuCO Agent AI Assessment

## Overview

DuCO Agent is an AI-powered healthcare claims processing system that automates document analysis, coordination of benefits (COB), and insurance pre-authorization generation.

The project uses FastAPI for the backend, React (Vite) for the frontend, OCR for document extraction, and Gemini AI for intelligent medical document analysis.

---

## Features

### 1. Document Analysis Agent

* Extracts text from PDF medical reports
* Extracts text from medical images using OCR (Tesseract)
* Identifies:

  * Diagnosis
  * Recommended Procedures
  * CPT Codes
  * Estimated Charges
  * Medical Necessity

### 2. Coordination of Benefits (COB) Agent

* Calculates primary insurance coverage
* Calculates secondary insurance coverage
* Computes patient out-of-pocket expenses
* Generates family-level cost summaries

### 3. Pre-Authorization Agent

* Generates insurance pre-authorization letters
* Supports multiple patients
* Uses Gemini AI for professional medical documentation
* Saves generated letters to output files

### 4. React Dashboard

* Connects to FastAPI backend
* Displays document analysis results
* Displays COB calculations
* Provides a simple healthcare claims dashboard

---

## Project Structure

```text
duco-agent-ai-assessment/
│
├── backend/
│   ├── agents/
│   │   ├── document_agent.py
│   │   ├── cob_agent.py
│   │   └── preauth_agent.py
│   │
│   ├── tools/
│   │   ├── pdf_parser.py
│   │   ├── image_parser.py
│   │   └── gemini_client.py
│   │
│   ├── tests/
│   ├── outputs/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── mock_data/
└── README.md
```

---

## Technologies Used

### Backend

* Python
* FastAPI
* Gemini API
* PyPDF2
* Tesseract OCR
* Pillow

### Frontend

* React
* Vite
* JavaScript
* CSS

### Version Control

* Git
* GitHub
* Feature Branch Workflow

---

## Installation

### Clone Repository

```bash
git clone https://github.com/isiri056/duco-agent-ai-assessment.git
cd duco-agent-ai-assessment
```

### Backend Setup

```bash
cd backend

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

```bash
cd frontend

npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "DuCO Agent Running"
}
```

### Analyze Documents

```http
GET /analyze
```

Returns:

* Document Analysis
* COB Results
* Pre-Authorization Letters

### Claims Calculation

```http
GET /claim
```

Returns insurance payment breakdown.

---

## Sample Workflow

1. Upload MRI report and invoice
2. Extract medical information
3. Generate CPT codes and diagnosis
4. Calculate insurance benefits
5. Generate pre-authorization letters
6. Display results on React dashboard

---

## Branch Strategy

* feature/document-parser
* feature/cob-agent
* feature/preauth-generator
* feature/ui-dashboard

All branches were merged into:

```text
feature/document-parser
```

---

## Author

**Isiri H S**

B.E. Computer Science and Engineering
RNS Institute of Technology

GitHub: https://github.com/isiri056
