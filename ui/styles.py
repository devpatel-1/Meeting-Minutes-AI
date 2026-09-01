CUSTOM_CSS = """
/* ==================================================
   MAIN PAGE
   ================================================== */

body {
    background: #080d1d;
}

.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}


/* ==================================================
   HEADER
   ================================================== */

.app-header {
    text-align: center;
    padding: 35px 20px 25px;
}

.app-header img {
    object-fit: contain;
    margin: 0 auto 15px auto;
}

.app-title {
    font-size: 42px;
    font-weight: 700;
    color: #f8fafc !important;
    margin-bottom: 10px;
}

.app-subtitle {
    font-size: 17px;
    color: #94a3b8 !important;
}

.app-header {
    text-align: center;
    padding: 35px 20px 25px;
}

.app-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #f8fafc;
}

.app-subtitle {
    font-size: 17px;
    color: #94a3b8;
}


/* ==================================================
   UPLOAD / CARD
   ================================================== */

.result-card {
    border-radius: 18px;
    padding: 22px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
}


/* IMPORTANT:
   Make text inside the white card dark
*/

.result-card {
    color: #1e293b;
}

.result-card h1,
.result-card h2,
.result-card h3,
.result-card p,
.result-card label {
    color: #1e293b !important;
}

.result-card h1,
.result-card h2,
.result-card h3,
.result-card p,
.result-card label {
    color: #1e293b !important;
}


/* ==================================================
   SECTION TITLES
   ================================================== */

.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
    color: #f8fafc;
}


/* ==================================================
   FOOTER
   ================================================== */

.app-footer {
    text-align: center;
    margin-top: 45px;
    margin-bottom: 25px;
    padding: 15px;
    color: #94a3b8;
    font-size: 14px;
}

.app-footer .heart {
    color: #ef4444;
}

.app-footer .author {
    color: #e2e8f0;
    font-weight: 600;
}


/* ==================================================
   HIDE DEFAULT GRADIO FOOTER
   ================================================== */

footer {
    display: none !important;
}
"""

