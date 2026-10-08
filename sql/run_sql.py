import sqlite3
import sys

path = sys.argv[1]
conn = sqlite3.connect(":memory:")
buffer = ""

with open(path, encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("--") and not buffer.strip():
            continue
        buffer += line
        if sqlite3.complete_statement(buffer):
            try:
                cur = conn.execute(buffer)
            except sqlite3.Error as e:
                print("ERROR:", e)
                print("In statement:", buffer.strip())
                break
            if cur.description:
                print(buffer.strip())
                print(" | ".join(c[0] for c in cur.description))
                for row in cur.fetchall():
                    print(" | ".join(str(v) for v in row))
                print()
            buffer = ""
