from django.shortcuts import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    # Get system details
    name = "Govind Sangal"  # Replace with your full name
    username = "codespace"
    
    # Get current IST time
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

    # Get 'top' command output (Linux/Mac)
    top_output = subprocess.getoutput('top -b -n 1')

    response = f"""
    <html>
    <head><title>System Monitor</title></head>
    <body>
        <h1>System Monitor</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {formatted_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)
