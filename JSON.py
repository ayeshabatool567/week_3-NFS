import json

response = '''
{
  "name":"Ali",
  "email":"ali123@gmail.com",
  "issue_type":"Password Reset",
  "urgency":"High",
  "summary":"User forgot password."
}
'''

try:
    data = json.loads(response)
    print("✅ Valid JSON")
    print(data)
except json.JSONDecodeError:
    print("❌ Invalid JSON")
