## Architecture Overview

1. User registers on platform
2. System collects location + activity data
3. Weather API provides real-time conditions
4. ML model predicts expected income
5. If income drops due to disruption → trigger claim
6. Payment processed via gateway

Components:
- Frontend: React
- Backend: Node.js (Express)
- ML Model: Python
- APIs: Weather API
