from models import db, Prompt

def get_prompt():
    prompt_from_db = db.session.query(Prompt).first()
    return prompt_from_db.content if prompt_from_db else None
