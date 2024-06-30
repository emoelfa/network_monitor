# src/threat_intelligence.py
import requests

API_KEY = 'YOUR_ABUSEIPDB_API_KEY'

def check_ip(ip):
    url = f'https://api.abuseipdb.com/api/v2/check'
    params = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def check_ips(ip_list):
    results = {}
    for ip in ip_list:
        result = check_ip(ip)
        results[ip] = result
    return results
