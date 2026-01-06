-- Detect repeated failed logons per user and ip
SELECT user, ip, COUNT(*) AS failures
FROM windows_logs
WHERE event_id = 4625
GROUP BY user, ip
HAVING failures >= 3;
