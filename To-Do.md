# To-Do List for Code Reviewer AI

## 🔧 Backend Tasks

- ✓ **User Authentication & Authorization**  
  - Implement login API for users  
  - Implement registration API for new users  
  - Manage session or token-based authentication 

- ✓ **Set up File Handling**
  - API for multiple file uploads
  - Validate `.py` file extensions and size

- ✓ **Codebase Parsing Module**
  - Read all files
  - Extract classes and functions (with hierarchy)

- ⬜ **Syntax Error Detection & Logging**
  - Detect syntax errors while parsing
  - Create error logs with filename, line, error type
  - Suggest corrected syntax

- ⬜ **Code Quality Analysis Engine**
  - Implement scoring rules (readability, modularity, docstrings, PEP8 compliance)
  - Return a score breakdown + total

- ⬜ **Improvement Suggestions Generator**
  - Suggest naming fixes, docstrings, modularity improvements
  - Provide short, actionable recommendations

- ⬜ **Export & Report Service**
  - Generate PDF/JSON reports containing structure, errors, quality score, suggestions

- ⬜ **Visualization Data API**
  - Prepare structured JSON for frontend charts/diagrams

---

## 🎨 Frontend Tasks

- ✓ **UI for Navbar**  
  - Create navigation bar layout 

- ✓ **UI for Login, Registration, Logout**  
  - Create login form UI  
  - Create registration form UI  
  - Include logout functionality and session management  

- ✓ **UI for File Upload**
  - multiple file selection
  - Show upload progress

- ⬜ **Display Extracted Code Structure**
  - Show tree view (File → Classes → Functions)
  - Expand/collapse hierarchy

- ⬜ **Error Reporting UI**
  - Show syntax errors with file name, line number, fix suggestions
  - Link to the corresponding part of the file if possible

- ⬜ **Code Quality Dashboard**
  - Display quality score (with breakdown)
  - Use progress bars or gauges

- ⬜ **Suggestions Panel**
  - List AI recommendations for improvement
  - Highlight which file/function suggestion belongs to

- ⬜ **Export & Download UI**
  - Button to download PDF/JSON reports
  - Indicate what’s included in the report

- ⬜ **Visualization Module**
  - Render charts for code quality metrics
  - Show tree diagrams for project structure
