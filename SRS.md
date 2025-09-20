# Software Requirement Specification (SRS)  
**Project Title**: Code Reviewer AI  
**Prepared by**: Md Abu Omayer Babu  
**Date**: ............  

---

## 1. Introduction  

### 1.1 Purpose  
The purpose of this document is to define the software requirements for **Code Reviewer AI**, a web-based system designed to analyze Python codebases. The system extracts class names and functions, detects syntax errors, generates a log of issues with correction suggestions, scores code quality, and provides professional recommendations to improve maintainability and readability.  

### 1.2 Scope  
Code Reviewer AI simplifies the process of reviewing Python projects by automatically analyzing uploaded files.  

- **Frontend**  
  - Supports multiple file upload.  
  - Displays extracted class-function hierarchy.  
  - Shows code quality results and improvement suggestions.  

- **Backend**  
  - Reads and parses Python code files.  
  - Extracts classes, functions, and hierarchy.  
  - Detects and logs syntax errors with suggested corrections.  
  - Analyzes code quality and assigns a score.  
  - Generates structured reports (PDF/JSON).  

**Future Scope**: Extend support to other languages, integrate with version control systems, and provide AI-powered refactoring.  

### 1.3 Definitions  
- **Syntax Error Log**: File containing the list of syntax errors detected in uploaded code.  
- **Code Quality Score**: Evaluation of code structure, readability, and maintainability.  
- **Professional Suggestions**: AI-generated advice to make the codebase follow best practices.  

### 1.4 References  
- IEEE Std 830-1998 – Recommended Practice for Software Requirements Specifications.  
- PEP 8 – Style Guide for Python Code.  

---

## 2. Overall Description  

### 2.1 Product Perspective  
- Web application with frontend and backend.  
- Backend exposes REST APIs for code analysis.  
- Optional database for storing uploaded files and reports.  

### 2.2 Product Functions  
- Upload multiple Python files.  
- Extract classes and functions (including nested under classes).  
- Detect syntax errors and log them with correction hints.  
- Suggest improvements to make the codebase professional.  
- Provide a code quality score.  
- Export results as reports.  

### 2.3 User Characteristics  
- Developers, students, and educators.  
- Basic understanding of Python programming.  

### 2.4 Constraints  
- Works only for Python code (initial release).  
- File upload limit (e.g., 5 MB per file).  
- Reports must be generated under 10 seconds for small projects.  

### 2.5 Assumptions and Dependencies  
- Users upload valid `.py` files.  
- Backend depends on Python parser libraries.  
- Internet access required to use the web application.  

---

## 3. Specific Requirements  

### 3.1 Functional Requirements  
1. **Multiple File Upload**  
   - Upload batch `.py` files.  

2. **Code Parsing & Extraction**  
   - Extract all classes and functions.  
   - Display hierarchy (File → Class → Functions).  

3. **Syntax Error Detection**  
   - Detect syntax errors in uploaded files.  
   - Create a log file with filename, line number, and error message.  
   - Suggest corrected syntax.  

4. **Code Quality Analysis**  
   - Score code based on readability, modularity, documentation, and PEP8 compliance.  
   - Provide breakdown and total score.  

5. **Improvement Suggestions**  
   - Naming convention corrections.  
   - Docstring/comment recommendations.  
   - Refactoring suggestions for better modularity and readability.  

6. **Export & Report Generation**  
   - Generate PDF/JSON reports containing:  
     - Extracted structure  
     - Syntax errors & corrections  
     - Code quality score  
     - Suggestions for improvement  

7. **Visualization**  
   - Prepare structured data for frontend tree diagrams and charts.  

### 3.2 Non-Functional Requirements  
- **Performance**: Analyze up to 20 files in < 10 seconds.  
- **Usability**: Clean, intuitive UI for uploading and reviewing.  
- **Security**: Uploaded files are only parsed, never executed.  
- **Scalability**: Designed for future support of additional languages.  

### 3.3 External Interface Requirements  
- **User Interface**: File upload form, structured results, downloadable reports.  
- **API Interface**: REST APIs for upload, parsing, scoring, and reporting.  
- **Hardware Interface**: Server with 4GB+ RAM and Python runtime.  

---

## 4. Features List

| Feature | Description | Status |
|---------|-------------|---------|
| Multiple File Upload | Upload multiple Python files at once for batch analysis | ✓ Completed |
| Parse Full Codebase | Analyze all uploaded files together | ✓ Completed |
| Extract Classes & Functions (Hierarchy) | Display structure in a tree format | ✓ Completed |
| Syntax Error Detection & Logging | Detect syntax errors, log with fixes | ⬜ Pending |
| Code Quality Scoring System | Assign score based on readability, modularity, documentation | ⬜ Pending |
| Professional Code Improvement Suggestions | Recommend best practices (naming, comments, modularity) | ⬜ Pending |
| Export Results (PDF/JSON Reports) | Generate structured reports | ⬜ Pending |
| Visualization (Tree Diagrams, Charts) | Visual representation of code hierarchy and metrics | ⬜ Pending |

### Future Enhancements

| Feature | Description | Status |
|---------|-------------|---------|
| Multi-Language Support | Support Java, JavaScript, C++ | ⬜ Planned |
| Advanced Metrics | Cyclomatic complexity, code duplication, maintainability index | ⬜ Planned |
| GitHub/GitLab Integration | Automated pull request reviews | ⬜ Planned |
| AI-Powered Code Refactoring | Smart recommendations for restructuring and optimizing code | ⬜ Planned |

---

## 5. Appendices  
- **Future Features**: Multi-language support, Git integration, AI-based refactoring, advanced metrics.  
- **Glossary**:  
  - *Code Structure Extraction*: Identifying classes and functions.  
  - *Multiple File Upload*: Uploading multiple files for batch analysis.  
