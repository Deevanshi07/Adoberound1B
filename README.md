# Connecting the Dots — Round 1B Pipeline

## Overview

This repository implements a pipeline to analyze PDF documents based on a target **persona** and **job-to-be-done** description. The system extracts structured sections from PDFs, scores them for relevance to the persona/job, and produces ordered JSON outputs highlighting the most pertinent sections and refined subsections.

The goal is to enable an MBA student (or any persona) to efficiently summarize and prioritize important content across multiple documents — particularly focusing on *company growth* in typical use-cases.

## Approach

### 1. PDF Section Extraction

- Use `pdfminer.six` to parse each PDF page and extract text blocks.
- Determine heading levels by clustering font sizes to identify headings (e.g., H1, H2, H3).
- Group text blocks into sections based on heading hierarchy.
- Assign titles, page numbers, heading levels, and aggregated section content.

### 2. Relevance Scoring

- Combine the persona and job description texts to form a query.
- Use TF-IDF vectorization (`scikit-learn`) to vectorize section contents and the query.
- Compute cosine similarity scores representing relevance of each section to the query.
- Attach scores to each section.

### 3. Refined Subsection Extraction

- For top-ranked sections per document, split section content into paragraphs.
- Score paragraphs similarly for finer-grained relevance.
- Extract and output top paragraphs as refined subsections for deeper insight.

### 4. Output Formatting

- Generate one JSON file per input PDF in an `output/` folder.
- Each JSON includes:
  - Metadata (documents, persona, job, timestamp)
  - Ranked sections with title, page, level, content, and score
  - Refined subsections extracted from the top sections

### Running with Docker

1. Build Docker image:
docker build -t adobe-round1bb:latest .

2. Run container:
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none adobe-round1bb:latest

3. Outputs will be in `output/` on your host system.

## Input Preparation

- `persona.txt`: Plain text describing the user persona who will consume the results (e.g., "MBA Student interested in company growth").
- `job.txt`: Plain text describing the task to accomplish (e.g., "Summarize and prioritize sections about company growth").
- PDFs: Text-based documents, preferably with clear headings and structured formats.

## Output Format

Each PDF produces a `.json` file.


