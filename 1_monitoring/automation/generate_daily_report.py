import sqlite3
from datetime import datetime

DB_PATH = "logs.db"
REPORT_PATH = "reports/sample_report.md"

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    query = """
    SELECT user, ip, COUNT(*) AS failure_count
    FROM windows_logs
    WHERE event_id = 4625
    GROUP BY user, ip
    HAVING failure_count >= 3;
    """

    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    with open(REPORT_PATH, "w") as f:
        f.write("# Daily Security Monitoring Report\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")

        if not rows:
            f.write("No suspicious failed logon bursts detected.\n")
        else:
            f.write("## Detected Failed Logon Bursts\n\n")
            f.write("| User | IP | Failure Count |\n")
            f.write("|------|----|---------------|\n")
            for user, ip, cnt in rows:
                f.write(f"| {user} | {ip} | {cnt} |\n")

if __name__ == "__main__":
    main()
