# Access Log Report Task

Parse the Apache-style access log and generate a JSON summary report with the following information:

## Success Criteria

1. **Report file created**: A valid JSON file is written to `/app/report.json`
2. **Total requests counted**: The `total_requests` field matches the actual line count in the log
3. **Unique IPs identified**: The `unique_ips` field reflects the count of distinct client IP addresses
4. **Top path found**: The `top_path` field contains the most frequently requested HTTP path

The report must be valid JSON and contain all three fields. The verifier will check both structure and accuracy of values.
