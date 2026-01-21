import yaml
import json
import re
import google.generativeai as genai

from db.equipment_repo import query_equipment
from db.pop_repo import query_pop
from db.schema import get_schema

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

EQUIPMENT_DB = config["database"]["equipment"]
POP_DB = config["database"]["pop"]

# Load schemas
EQUIPMENT_SCHEMA = get_schema(EQUIPMENT_DB)
POP_SCHEMA = get_schema(POP_DB)

genai.configure(api_key="AIzaSyB9F1zmj5i7xhBmz2K1IqlTdL49tD62Brw")
model = genai.GenerativeModel(config["model"]["name"])

SYSTEM_PROMPT = f"""
You are an expert SQLite assistant.

You MUST use ONLY the following schemas.

EQUIPMENT DATABASE SCHEMA:
{json.dumps(EQUIPMENT_SCHEMA, indent=2)}

POP DATABASE SCHEMA:
{json.dumps(POP_SCHEMA, indent=2)}

STRICT RULES:
- Use ONLY column names from schema
- NEVER invent columns
- NEVER use SELECT *
- SQLite compatible SQL only
- No markdown
- No explanations
- Output ONLY valid JSON

JSON FORMAT:
{{
  "database": "equipment | pop",
  "sql": "SQL QUERY HERE",
  "params": []
}}
"""

def extract_json(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("LLM did not return valid JSON")
    return json.loads(match.group())

def process_query(user_query: str):
    prompt = SYSTEM_PROMPT + "\nUser Query: " + user_query
    response = model.generate_content(prompt)

    try:
        data = extract_json(response.text)
    except Exception:
        raise ValueError(f"Invalid LLM response:\n{response.text}")

    db = data["database"]
    sql = data["sql"]
    params = data.get("params", [])

    try:
        if db == "equipment":
            columns, rows = query_equipment(EQUIPMENT_DB, sql, params)
        elif db == "pop":
            columns, rows = query_pop(POP_DB, sql, params)
        else:
            raise ValueError("Invalid database name")

    except Exception as e:
        raise ValueError(f"SQL Execution Error: {e}\nSQL: {sql}")

    if not rows:
        return "No results found."

    return [dict(zip(columns, row)) for row in rows]