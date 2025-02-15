import re

def is_suspicious_url(url):
    # Common phishing/hacking patterns
    suspicious_patterns = [
        r"\b(login|verify|update|secure|account)\b",  # Phishing keywords
        r"@|%40",  # Encoding tricks
        r"https?://.*\..*\..*\..*",  # Too many subdomains
        r"https?://\d+\.\d+\.\d+\.\d+",  # IP-based URLs
        r"https?://.*\?.*=",  # Query manipulation
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return True
    return False

# Prompt the user for a URL
url = input("Enter the URL you want to check: ")

# Check if the URL is suspicious
if is_suspicious_url(url):
    print(f"⚠️ Suspicious URL detected: {url}")
else:
    print(f"✅ Safe URL: {url}")