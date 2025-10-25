#!/usr/bin/env python3
"""
DevOps Sample Application
"""

def main():
    print("Hello, Elevates Labs!")
    print("This is project3 representing  sample application for demonstrating Git best practices.")

if __name__ == "__main__":
    main()
EOF

# Create configuration file
cat > config/settings.yaml << 'EOF'
app:
  name: "DevOps Sample App"
  version: "1.0.0"
  environment: "development"

server:
  host: "0.0.0.0"
  port: 8080

logging:
  level: "INFO"
  format: "json"
EOF

# Create deployment script
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash
# Deployment script for DevOps project

echo "Starting deployment..."
echo "Environment: $1"

# Add your deployment logic here
python src/app.py

echo "Deployment completed!"
EOF

chmod +x scripts/deploy.sh

# Create test file
cat > tests/test_app.py << 'EOF'
"""
Unit tests for the application
"""
import unittest
from src import app

class TestApp(unittest.TestCase):
    def test_main(self):
        """Test main function exists"""
        self.assertTrue(callable(app.main))

if __name__ == '__main__':
    unittest.main()
