# src/log_parser.py
import re

def parse_log_file(log_file_path):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)')
    with open(log_file_path, 'r') as log_file:
        logs = log_file.readlines()
    
    connections = []
    for log in logs:
        match = pattern.search(log)
        if match:
            connections.append({
                'remote_ip': match.group(1),
                'port': match.group(2)
            })
    return connections
