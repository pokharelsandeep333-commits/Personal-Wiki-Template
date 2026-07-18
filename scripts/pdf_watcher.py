import os
import sys
import time
import shutil
import datetime
import re
import argparse
try:
    import pymupdf4llm
except ImportError:
    print("Error: pymupdf4llm is not installed. Run: pip install pymupdf4llm")
    sys.exit(1)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PDF_DIR = os.path.join("Raw", "PDFs")
SOURCES_DIR = os.path.join("Raw", "Sources")
FILES_DIR = os.path.join("Raw", "Files")

def sanitize_title(filename):
    """Converts filename to a clean, ASCII-only title for the Wiki."""
    # Remove extension
    name = os.path.splitext(filename)[0]
    # Keep only ASCII alphanumeric and spaces/dashes/underscores
    name = re.sub(r'[^\x00-\x7F]+', '', name) # Remove non-ASCII
    name = re.sub(r'[^a-zA-Z0-9\s\-_]', '', name)
    name = ' '.join(name.split()) # Remove extra whitespace
    return name or "Untitled_PDF"

def process_pdf(filepath):
    """Converts a PDF to Markdown and saves it to Raw/Sources."""
    if not os.path.exists(filepath) or not filepath.lower().endswith('.pdf'):
        return

    filename = os.path.basename(filepath)
    title = sanitize_title(filename)
    print(f"Processing PDF: {filename} -> {title}.md")

    try:
        # Convert PDF to Markdown
        md_text = pymupdf4llm.to_markdown(filepath)
        
        # Build standard LLM-Wiki Frontmatter
        frontmatter = f"""---
Title: "{title}"
Reference: "{filename}"
Created: {datetime.date.today().isoformat()}
tags:
  - "source"
Processed: false
---
"""
        final_content = frontmatter + "\n" + md_text
        
        # Save to Raw/Sources
        out_path = os.path.join(SOURCES_DIR, f"{title}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"Saved extracted markdown to: {out_path}")
        
        # Archive original PDF to Raw/Files
        archive_path = os.path.join(FILES_DIR, filename)
        # Handle duplicates in archive
        if os.path.exists(archive_path):
            base, ext = os.path.splitext(filename)
            archive_path = os.path.join(FILES_DIR, f"{base}_{int(time.time())}{ext}")
            
        shutil.move(filepath, archive_path)
        print(f"Archived original PDF to: {archive_path}")
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")

def scan_directory():
    """Scans the PDF drop zone and processes all PDFs."""
    print(f"Scanning {PDF_DIR} for new PDFs...")
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR)
        
    count = 0
    for file in os.listdir(PDF_DIR):
        if file.lower().endswith('.pdf'):
            process_pdf(os.path.join(PDF_DIR, file))
            count += 1
            
    if count == 0:
        print("No new PDFs found.")
    else:
        print(f"Successfully processed {count} PDFs.")

class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith('.pdf'):
            # Wait a moment to ensure file is fully copied before processing
            time.sleep(1)
            process_pdf(event.src_path)

def start_watcher():
    """Starts a persistent watcher on the PDF drop zone."""
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR)
        
    event_handler = PDFHandler()
    observer = Observer()
    observer.schedule(event_handler, PDF_DIR, recursive=False)
    observer.start()
    
    print(f"Watching {PDF_DIR} for new PDFs. Press Ctrl+C to stop...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF to Markdown Ingestion Pipeline")
    parser.add_argument("--watch", action="store_true", help="Run continuously and watch for new PDFs")
    args = parser.parse_args()
    
    # Ensure directories exist
    for d in [PDF_DIR, SOURCES_DIR, FILES_DIR]:
        os.makedirs(d, exist_ok=True)
        
    if args.watch:
        start_watcher()
    else:
        scan_directory()
