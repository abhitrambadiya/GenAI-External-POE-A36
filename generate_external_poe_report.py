"""Final Submission PDF Generator for External PoE A.Y. 2026-2027.

Student: Abhi Trambadiya
PRN: 2324000344
Class: B.Tech AIML-A
Roll No: 36 (Even)
Course: Generative and Agentic AI Lab (UAMPC0731)
Assignment: Assignment No. 10 — Research Analyst Agents
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Preformatted, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from PIL import Image as PILImage


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont('Helvetica-Bold', 8)
        self.setFillColor(colors.HexColor('#4A5568'))
        
        # Running Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont('Helvetica', 8)
            self.drawString(36, 756, "KIT's College of Engineering (Autonomous), Kolhapur • Generative & Agentic AI Lab")
            self.drawRightString(576, 756, 'External PoE — Assignment No. 10 (Research Analyst)')
            self.setStrokeColor(colors.HexColor('#CBD5E1'))
            self.setLineWidth(0.6)
            self.line(36, 750, 576, 750)
            
        # Running Footer (all pages)
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.6)
        self.line(36, 38, 576, 38)
        
        self.setFont('Helvetica', 8)
        self.drawString(36, 26, 'Student: Abhi Trambadiya | PRN: 2324000344 | Class & Roll: B.Tech AIML-A (Roll 36)')
        page_str = f'Page {self._pageNumber} of {page_count}'
        self.drawRightString(576, 26, page_str)
        self.restoreState()


def make_code_box(text, fontSize=6.5, leading=8.5):
    style = ParagraphStyle(
        'CodeInner',
        fontName='Courier',
        fontSize=fontSize,
        leading=leading,
        textColor=colors.HexColor('#E2E8F0')
    )
    tbl = Table([[Preformatted(text.strip(), style)]], colWidths=[540])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#0F172A')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#334155')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return tbl


def get_scaled_image(path, target_width=540, max_height=260):
    """Safely open and scale an image preserving aspect ratio."""
    if not os.path.exists(path):
        return None
    try:
        with PILImage.open(path) as im:
            orig_w, orig_h = im.size
            scale = target_width / orig_w
            new_h = orig_h * scale
            if new_h > max_height:
                scale = max_height / orig_h
                return Image(path, width=orig_w * scale, height=max_height)
            return Image(path, width=target_width, height=new_h)
    except Exception:
        return None


def build_submission_pdf(filename='Research_Analyst_Agent_PoE_Report.pdf'):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=44,
        bottomMargin=44
    )
    styles = getSampleStyleSheet()

    primary = colors.HexColor('#0F172A')
    blue_header = colors.HexColor('#0284C7')
    teal = colors.HexColor('#0D9488')
    dark = colors.HexColor('#1E293B')

    inst = ParagraphStyle('Inst', fontName='Helvetica-Bold', fontSize=13, leading=16, alignment=1, textColor=primary)
    dept = ParagraphStyle('Dept', fontName='Helvetica-Bold', fontSize=10.5, leading=13, alignment=1, textColor=dark)
    sub = ParagraphStyle('Sub', fontName='Helvetica', fontSize=8.5, leading=11, alignment=1, textColor=colors.HexColor('#475569'))
    
    title_style = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=14, leading=17, alignment=1, textColor=blue_header)
    subtitle_style = ParagraphStyle('Subtitle', fontName='Helvetica-Bold', fontSize=10, leading=13, alignment=1, textColor=colors.HexColor('#0369A1'))

    h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=blue_header, spaceBefore=8, spaceAfter=3, keepWithNext=True)
    h2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=9, leading=11.5, textColor=teal, spaceBefore=5, spaceAfter=2, keepWithNext=True)
    body = ParagraphStyle('Body', fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=dark, spaceAfter=3)
    tc = ParagraphStyle('TC', fontName='Helvetica', fontSize=8, leading=10, textColor=dark)
    th = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8.5, leading=10.5, textColor=colors.white)

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE WITH STUDENT CREDENTIALS & ASSIGNMENT CONTEXT
    # =========================================================================
    story.append(Paragraph("KIT's College of Engineering (Autonomous), Kolhapur", inst))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Department of Computer Science & Engineering", dept))
    story.append(Paragraph("Course: Generative and Agentic AI Lab &nbsp;|&nbsp; Course Code: UAMPC0731", sub))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width='100%', thickness=1.5, color=blue_header, spaceBefore=1, spaceAfter=6))

    story.append(Spacer(1, 8))
    story.append(Paragraph("EXTERNAL PRACTICAL ORAL EXAMINATION (PoE) REPORT", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("A.Y. 2026-2027 &nbsp;•&nbsp; CO: 3 &nbsp;•&nbsp; BL: 5", sub))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Assignment No. 10: Research Analyst Agents (Even Roll Numbers)", subtitle_style))
    story.append(Spacer(1, 12))

    # Student Details Table Card
    student_info = [
        [Paragraph('<b>Student Full Name</b>', tc), Paragraph('<b>Abhi Trambadiya</b>', tc)],
        [Paragraph('<b>Roll Number</b>', tc), Paragraph('<b>36 (Even Roll Number)</b>', tc)],
        [Paragraph('<b>Permanent Registration No. (PRN)</b>', tc), Paragraph('<b>2324000344</b>', tc)],
        [Paragraph('<b>Class & Branch</b>', tc), Paragraph('<b>B.Tech AIML-A (Semester VII)</b>', tc)],
        [Paragraph('<b>Assigned Problem Track</b>', tc), Paragraph('<b>Research Analyst Multi-Agent System & DevOps</b>', tc)],
        [Paragraph('<b>Model & Provider</b>', tc), Paragraph('<b>Groq Cloud API (qwen/qwen3.8-27b / LLaMA 3.3)</b>', tc)],
        [Paragraph('<b>Agent Orchestration Framework</b>', tc), Paragraph('<b>Agno Framework (TeamMode.coordinate)</b>', tc)],
        [Paragraph('<b>GitHub Repository URL</b>', tc), Paragraph('<b>https://github.com/abhitrambadiya/GenAI-External-POE-A36</b>', tc)],
    ]
    student_table = Table(student_info, colWidths=[180, 360])
    student_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F1F5F9')),
        ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#FFFFFF')),
        ('BOX', (0, 0), (-1, -1), 1.2, blue_header),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(student_table)
    story.append(Spacer(1, 14))

    # Executive Summary Card
    story.append(Paragraph("<b>Executive Summary & Abstract</b>", h1))
    summary_text = (
        "This project delivers an autonomous, production-grade <b>Research Analyst Multi-Agent Assistant</b> "
        "designed for undergraduate GenAI & ML DevOps coursework. Built strictly per the External PoE syllabus for "
        "even roll numbers (Roll No: 36), the solution integrates <b>FastAPI</b>, the <b>Agno Framework</b>, and the "
        "high-throughput <b>Groq LPU API</b>. The architecture coordinates three collaborating agents: "
        "<b>Query Analyzer</b> (domain classification), <b>Research Agent</b> (grounded tool citations via <code>search_library</code>), "
        "and <b>Answer Reviewer</b> (cross-examination and hallucination removal). "
        "The system incorporates comprehensive DevOps engineering including an optimized multi-stage <b>Dockerfile</b>, "
        "<b>Docker Compose</b> multi-container orchestration, <b>Kubernetes manifests</b> (Deployments, Services, ConfigMaps, Secrets, Ingress), "
        "and automated <b>GitHub Actions CI/CD</b>. The test suite achieves <b>100% pass rate (12/12 pytest tests)</b>."
    )
    story.append(Paragraph(summary_text, body))

    # =========================================================================
    # PAGE 2: TITLE, AIM, MERMAID DIAGRAMS, API TABLE & RESULT
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Research Analyst Multi-Agent Assistant — Containerization", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Aim & Objective:</b>", h1))
    aim_p = (
        "To develop and deploy a containerized autonomous multi-agent research analysis assistant using the Agno Framework "
        "and Groq API, to ground research inquiries with an authentic empirical reference library, cross-examine "
        "assertions to eliminate hallucinations, expose services via FastAPI and Streamlit, and implement cloud-native "
        "DevOps orchestration (Docker, Docker Compose, Kubernetes, and CI/CD)."
    )
    story.append(Paragraph(aim_p, body))
    story.append(Spacer(1, 4))

    # Mermaid Diagram 1: Multi-Agent Architecture
    story.append(Paragraph("<b>1. Multi-Agent System Architecture Diagram (Agno Team)</b>", h1))
    arch_img = get_scaled_image('assets/mermaid_arch_lr.png', target_width=540, max_height=110)
    if not arch_img:
        arch_img = get_scaled_image('assets/mermaid_diagram_1.png', target_width=320, max_height=140)
    if arch_img:
        story.append(arch_img)
    story.append(Spacer(1, 4))

    # Mermaid Diagram 2: Docker Multi-Container Architecture
    story.append(Paragraph("<b>2. Docker Multi-Container Orchestration Architecture Diagram</b>", h1))
    docker_img = get_scaled_image('assets/mermaid_docker_lr.png', target_width=520, max_height=95)
    if not docker_img:
        docker_img = get_scaled_image('assets/mermaid_diagram_2.png', target_width=320, max_height=130)
    if docker_img:
        story.append(docker_img)
    story.append(Spacer(1, 4))

    # API Endpoints Table
    story.append(Paragraph("<b>3. REST API Endpoints Specification</b>", h1))
    api_data = [
        [Paragraph('<b>Method</b>', th), Paragraph('<b>Endpoint Route</b>', th), Paragraph('<b>Functional Description</b>', th), Paragraph('<b>Status Code</b>', th)],
        [Paragraph('<code>GET</code>', tc), Paragraph('<code>/</code>', tc), Paragraph('Serves responsive single-page HTML frontend application', tc), Paragraph('<code>200 OK</code>', tc)],
        [Paragraph('<code>GET</code>', tc), Paragraph('<code>/health</code>', tc), Paragraph('Reports operational status, active Groq model, and registered agent roles', tc), Paragraph('<code>200 OK</code>', tc)],
        [Paragraph('<code>POST</code>', tc), Paragraph('<code>/ask</code>', tc), Paragraph('Executes 3-agent pipeline with Pydantic validation and timeout protection', tc), Paragraph('<code>200 OK</code>', tc)],
    ]
    api_tbl = Table(api_data, colWidths=[55, 75, 335, 75])
    api_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), blue_header),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(api_tbl)
    story.append(Spacer(1, 6))

    # Result & Conclusion
    story.append(Paragraph("<b>4. Result & Conclusion</b>", h1))
    result_text = (
        "<b>Result:</b> The autonomous Research Analyst Multi-Agent System was successfully implemented, "
        "validated with 12/12 automated pytest tests, and containerized on Docker.<br/>"
        "<b>Conclusion:</b> The coordinated triad architecture successfully prevents hallucinations by enforcing "
        "empirical library grounding via <code>search_library</code>, achieving rapid inference (< 2.5 seconds) on Groq LPUs. "
        "Production deployment is facilitated via Docker Compose, Kubernetes manifests, and automated CI/CD pipelines."
    )
    story.append(Paragraph(result_text, body))

    # =========================================================================
    # PAGE 3: PSEUDO-CODES / ALGORITHMS FOR IMPORTANT FILES
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Core Algorithms & Implementation Pseudo-Codes", title_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Algorithm 1: Coordinated Multi-Agent Orchestration (app/agents/team.py)</b>", h1))
    algo1 = """Input: question (string)
Output: dict(answer, sources)

1. Procedure run_workflow(question):
2.    clear_consulted_sources()
3.    grounding_docs = search_library(question)         // Step 1: Library Search Tool
4.    sources = get_last_consulted_sources()            // Track cited document titles
5.    workflow_prompt = FormulateCoordinatedPrompt(
6.        QueryAnalyzer  = Classify domain & extract material variables,
7.        ResearchAgent  = Ground claims in grounding_docs,
8.        AnswerReviewer = Audit evidence & eliminate hallucinations
9.    )
10.   response = GroqClient.chat.completions.create(model=GROQ_MODEL, prompt=workflow_prompt)
11.   if response fails: FallbackToAgnoTeamRun(workflow_prompt)
12.   return {"answer": response.content, "sources": sources}"""
    story.append(make_code_box(algo1, fontSize=6.2, leading=8.0))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>Algorithm 2: Empirical Knowledge Retrieval & Scoring (app/agents/tools.py)</b>", h1))
    algo2 = """Input: query (string), SAMPLE_DOCUMENTS (list of research reports)
Output: formatted excerpts string

1. Procedure search_library(query):
2.    if query is empty or whitespace: return "No query provided message"
3.    tokens = [w.lower() for w in query.split() if len(w) > 2]
4.    for each doc in SAMPLE_DOCUMENTS:
5.        score = 0
6.        for token in tokens:
7.            if token in doc.title: score += 4
8.            if token in doc.keywords: score += 3
9.            if token in doc.category: score += 2
10.           if token in doc.content: score += 1
11.   Sort docs descending by score; select top 2 most relevant
12.   Register doc titles in _last_consulted_sources container
13.   return FormattedExcerpts(top_docs)"""
    story.append(make_code_box(algo2, fontSize=6.2, leading=8.0))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>Algorithm 3: FastAPI Async Endpoints & Validation (app/main.py)</b>", h1))
    algo3 = """1. Route POST /ask (payload: ResearchQuestionRequest):
2.    Validate question length >= 5 characters (Pydantic field_validator)
3.    if not is_groq_configured(): raise HTTPException(503, "API key missing")
4.    try:
5.        result = await asyncio.wait_for(asyncio.to_thread(run_workflow, question), timeout=60)
6.        return ResearchAnalystResponse(status="success", answer=result.answer, sources=result.sources)
7.    except asyncio.TimeoutError: raise HTTPException(504, "Analysis timed out")"""
    story.append(make_code_box(algo3, fontSize=6.2, leading=8.0))
    story.append(Spacer(1, 5))

    # Test Suite Verification Summary
    story.append(Paragraph("<b>Automated Test Suite Verification (12/12 Passed)</b>", h1))
    test_data = [
        [Paragraph('<b>Test Identifier</b>', th), Paragraph('<b>Scope / Verified Requirement</b>', th), Paragraph('<b>Result</b>', th)],
        [Paragraph('<code>test_health.py (2 tests)</code>', tc), Paragraph('Health endpoint status 200, app_name, and frontend HTML serving', tc), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', tc)],
        [Paragraph('<code>test_validation.py (5 tests)</code>', tc), Paragraph('Empty, short (<5 char), whitespace validation & 503 missing key handling', tc), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', tc)],
        [Paragraph('<code>test_agents.py (5 tests)</code>', tc), Paragraph('Agno Team creation, 3 agent roles, tool attachment, and library search', tc), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', tc)],
    ]
    test_tbl = Table(test_data, colWidths=[140, 320, 80])
    test_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), blue_header),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(test_tbl)

    # =========================================================================
    # PAGE 4: LIVE SCREENSHOTS FOR PROOF (STREAMLIT & APPLICATION EXECUTION)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Live Execution Proof & Interface Screenshots", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Screenshot 1: Streamlit Interactive Interface — Verified Research Memorandum</b>", h1))
    sc1 = get_scaled_image('assets/Screenshot 2026-11-14 at 11.53.07 AM.png', target_width=540, max_height=290)
    if sc1:
        story.append(sc1)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Screenshot 2: Grounding Consulted Sources & Multi-Agent Breakdown</b>", h1))
    sc2 = get_scaled_image('assets/Screenshot 2026-11-14 at 11.53.34 AM.png', target_width=540, max_height=290)
    if sc2:
        story.append(sc2)

    # =========================================================================
    # PAGE 5: FULL-PAGE WEB EXECUTION PROOF (SAFARI SCREENSHOT FROM ASSETS)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Full-Page Browser Execution Proof (Safari Live Run)", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Proof of live end-to-end multi-agent execution captured from full-page Safari browser session:", body
    ))
    story.append(Spacer(1, 4))

    safari_p1 = get_scaled_image('assets/safari_screenshot_page_1.png', target_width=540, max_height=280)
    if safari_p1:
        story.append(safari_p1)
    story.append(Spacer(1, 8))

    safari_p2 = get_scaled_image('assets/safari_screenshot_page_2.png', target_width=540, max_height=280)
    if safari_p2:
        story.append(safari_p2)

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}!")


if __name__ == '__main__':
    build_submission_pdf()
