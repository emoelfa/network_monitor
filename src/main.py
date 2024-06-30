# src/main.py
from network_info import get_current_connections
from log_parser import parse_log_file
from threat_intelligence import check_ips

def format_result(result):
    if 'data' in result:
        data = result['data']
        formatted_result = (
            f"IP Address: {data.get('ipAddress', 'N/A')}\n"
            f"  - Is Public: {data.get('isPublic', 'N/A')}\n"
            f"  - IP Version: {data.get('ipVersion', 'N/A')}\n"
            f"  - Is Whitelisted: {data.get('isWhitelisted', 'N/A')}\n"
            f"  - Abuse Confidence Score: {data.get('abuseConfidenceScore', 'N/A')}\n"
            f"  - Country Code: {data.get('countryCode', 'N/A')}\n"
            f"  - Usage Type: {data.get('usageType', 'N/A')}\n"
            f"  - ISP: {data.get('isp', 'N/A')}\n"
            f"  - Domain: {data.get('domain', 'N/A')}\n"
            f"  - Hostnames: {', '.join(data.get('hostnames', ['N/A']))}\n"
            f"  - Is Tor: {data.get('isTor', 'N/A')}\n"
            f"  - Total Reports: {data.get('totalReports', 'N/A')}\n"
            f"  - Number of Distinct Users: {data.get('numDistinctUsers', 'N/A')}\n"
            f"  - Last Reported At: {data.get('lastReportedAt', 'N/A')}\n"
        )
    else:
        formatted_result = "No 'data' key found in result.\n"

    return formatted_result

def main():
    current_connections = get_current_connections()
    log_connections = parse_log_file(r'/path/to/your/logfile.log')
    unique_ips = set()
    for conn in current_connections:
        unique_ips.add(conn['remote_address'].split(':')[0])
    for conn in log_connections:
        unique_ips.add(conn['remote_ip'])
    
    results = check_ips(list(unique_ips))
    for ip, result in results.items():
        print(f"IP: {ip}")
        formated_result = format_result(result)
        print(formated_result)
        

if __name__ == "__main__":
    main()
