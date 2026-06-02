import os
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict
from pipeline.solution_table_exporter import parse_markdown_table_rows

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "review.db")

def get_connection():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_review_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS review_items (
                problem_number TEXT PRIMARY KEY,
                problem_title TEXT NOT NULL,
                last_viewed TEXT,
                tags TEXT,
                pattern_solution TEXT,
                when_to_use TEXT,
                mastery_level INTEGER DEFAULT 0,
                mistake_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'new',
                notes TEXT DEFAULT '',
                code_path TEXT DEFAULT '',
                raw_table_row TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        conn.commit()

def row_to_dict(row: sqlite3.Row) -> Dict:
    return dict(row)

def list_review_items() -> List[Dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT *
            FROM review_items
            ORDER BY updated_at DESC
            """
        ).fetchall()
        return [row_to_dict(row) for row in rows]

def get_review_item(problem_number: str) -> Optional[Dict]:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT *
            FROM review_items
            WHERE problem_number = ?
            """,
            (str(problem_number),),
        ).fetchone()

        if not row:
            return None

        return row_to_dict(row)
    
def parse_review_item_from_table(table_text: str) -> Optional[Dict]:
    rows = parse_markdown_table_rows(table_text)
    if not rows:
        return None

    row = rows[0]

    return {
        "problem_number": str(int(row[0])),
        "problem_title": row[1],
        "last_viewed": row[2],
        "tags": row[3],
        "pattern_solution": row[4],
        "when_to_use": row[5],
        "raw_table_row": "|".join(row),
    }