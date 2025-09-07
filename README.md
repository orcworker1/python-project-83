<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Analyzer - README</title>
</head>
<p>
        <a href="https://github.com/orcworker1/python-project-83/actions">
            <img src="https://github.com/orcworker1/python-project-83/actions/workflows/hexlet-check.yml/badge.svg" alt="Actions Status">
        </a>
    </p>
<body>
    <h1>Hi there, I'm Valentin <img src="../tinymce/plugins/emoticons/img/smiley-wink.gif" alt="wink" /></h1>
    <h1>This is my second project: Page analyzer</h1>
    <p><strong>Demo:</strong> <a href="https://page-analyzer-o462.onrender.com">https://page-analyzer-o462.onrender.com</a></p>
    <p>Web application for analyzing pages for SEO suitability. Provides functionality similar to PageSpeed Insights by checking URLs and extracting important SEO elements.</p>
    <h2>Project Structure</h2>
    <ul>
        <li><code>page_analyzer/app.py</code> - Flask application routes</li>
        <li><code>page_analyzer/parse.py</code> - HTML parsing functions</li>
        <li><code>page_analyzer/templates/</code> - Jinja2 HTML templates</li>
    </ul>
    <h3>Setup</h3>
    <ol>
        <li>Clone the repository:
            <pre>git clone https://github.com/orcworker1/python-project-83.git
cd python-project-83</pre>
        </li>
        <li>Install dependencies:
            <pre>make install</pre>
        </li>
        <li>Set up environment variables:
            <pre>cp .env.example .env
</pre>
        </li>
        <li>Create database tables:
            <pre>psql -d your_database -f database.sql</pre>
        </li>
    </ol>
    <h2>Usage</h2>
    <h3>Development</h3>
    <pre>make dev</pre>
    <p>Application will be available at <a href="http://localhost:5000">http://localhost:5000</a></p>
    <h3>Production</h3>
    <pre>make start</pre>
    <h2>Dependencies</h2>
    <h3>Core Framework</h3>
    <ul>
        <li><strong>Flask 3.1.1</strong> - Web framework for Python</li>
        <li><strong>Jinja2</strong> - Template engine (Flask dependency)</li>
        <li><strong>Werkzeug</strong> - WSGI utility library (Flask dependency)</li>
    </ul>
    <h3>Database</h3>
    <ul>
        <li><strong>postgres 4.0</strong> - PostgreSQL connection utilities</li>
    </ul>
    <h3>Web Scraping & Validation</h3>
    <ul>
        <li><strong>requests 2.32.4</strong> - HTTP library for making requests</li>
        <li><strong>beautifulsoup4 4.13.4</strong> - HTML parsing and scraping</li>
        <li><strong>validators 0.35.0</strong> - URL validation utilities</li>
    </ul>
</body>
</html>