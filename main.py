import os

from src.pdf_parser import extract_sections
from src.output_formatter import build_output_json

def load_persona_and_job(input_dir='input'):
    with open(os.path.join(input_dir, 'persona.txt'), 'r', encoding='utf-8') as f:
        persona = f.read().strip()
    with open(os.path.join(input_dir, 'job.txt'), 'r', encoding='utf-8') as f:
        job = f.read().strip()
    return persona, job

def get_pdf_files(input_dir='input'):
    return [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]

def main():
    input_dir = 'input'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    persona, job = load_persona_and_job(input_dir)
    pdf_files = get_pdf_files(input_dir)
    pdf_filenames = [os.path.basename(p) for p in pdf_files]

    all_sections = []
    for pdf_path in pdf_files:
        doc_name = os.path.basename(pdf_path)
        data = extract_sections(pdf_path)
        for sec in data.get('sections', []):
            sec['document'] = doc_name
        all_sections.extend(data.get('sections', []))

    build_output_json(pdf_filenames, persona, job, all_sections, output_dir)
    print(f"Done! Output files are in '{output_dir}/'.")

if __name__ == "__main__":
    main()
