import re
with open('equality.html', 'r') as f:
    data = f.read()
    print(re.findall(r'([^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z])', data))
f.closed
