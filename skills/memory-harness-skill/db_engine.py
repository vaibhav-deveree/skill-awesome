import sqlite3
import argparse
import sys
import os
import json
from datetime import datetime

DB_PATH = ".memory/memory.db"

def init_db():
    if not os.path.exists(".memory"):
        os.makedirs(".memory")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # User Intent Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS intent (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            category TEXT,
            content TEXT
        )
    ''')
    
    # Current State / Tasks
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS state (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            status TEXT,
            task TEXT,
            assigned_to TEXT
        )
    ''')
    
    # History
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            completed_task TEXT,
            outcome TEXT
        )
    ''')
    
    # Changelog
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS changelog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            file_changed TEXT,
            description TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def log_entry(table, data_dict):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    data_dict['timestamp'] = datetime.now().isoformat()
    columns = ', '.join(data_dict.keys())
    placeholders = ', '.join('?' * len(data_dict))
    values = tuple(data_dict.values())
    
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print(f"Logged to {table} successfully.")

def run_query(sql_query):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        if sql_query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            results = [dict(row) for row in rows]
            print(json.dumps(results, indent=2))
        else:
            conn.commit()
            print("Query executed successfully.")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()

def main():
    parser = argparse.ArgumentParser(description="Memory Harness DB Engine")
    subparsers = parser.add_subparsers(dest="command")
    
    # Init
    subparsers.add_parser("init", help="Initialize the database")
    
    # Log Intent
    parser_intent = subparsers.add_parser("log_intent")
    parser_intent.add_argument("--category", required=True, help="Category of intent (e.g., 'feature', 'bug', 'user_said')")
    parser_intent.add_argument("--content", required=True, help="What the user wants or said")
    
    # Log State
    parser_state = subparsers.add_parser("log_state")
    parser_state.add_argument("--status", required=True, help="e.g., 'TODO', 'IN_PROGRESS', 'BLOCKED'")
    parser_state.add_argument("--task", required=True, help="Task description")
    parser_state.add_argument("--assigned_to", default="unassigned", help="Agent or team assigned")
    
    # Log History
    parser_history = subparsers.add_parser("log_history")
    parser_history.add_argument("--task", required=True, help="Completed task")
    parser_history.add_argument("--outcome", required=True, help="Outcome or notes")
    
    # Log Changelog
    parser_changelog = subparsers.add_parser("log_changelog")
    parser_changelog.add_argument("--file", required=True, help="File changed")
    parser_changelog.add_argument("--description", required=True, help="What was changed")
    
    # Query
    parser_query = subparsers.add_parser("query")
    parser_query.add_argument("sql", help="Raw SQL query")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_db()
        print("Database initialized.")
    elif args.command == "log_intent":
        log_entry("intent", {"category": args.category, "content": args.content})
    elif args.command == "log_state":
        log_entry("state", {"status": args.status, "task": args.task, "assigned_to": args.assigned_to})
    elif args.command == "log_history":
        log_entry("history", {"completed_task": args.task, "outcome": args.outcome})
    elif args.command == "log_changelog":
        log_entry("changelog", {"file_changed": args.file, "description": args.description})
    elif args.command == "query":
        run_query(args.sql)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
