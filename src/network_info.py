# src/network_info.py
import psutil

def get_current_connections():
    connections = psutil.net_connections(kind='inet')
    current_connections = []
    for conn in connections:
        if conn.raddr:
            current_connections.append({
                'local_address': f"{conn.laddr.ip}:{conn.laddr.port}",
                'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}",
                'status': conn.status
            })
    return current_connections
