# Legal Prejudice Analysis API Documentation

This documentation provides comprehensive information about the Legal Prejudice Analysis API, which allows you to integrate prejudice risk assessment capabilities into your own applications and systems.

## API Overview

The Legal Prejudice Analysis API is a RESTful service that provides:

- Risk assessment calculations
- Factor analysis
- Historical data tracking
- Report generation
- Case management integration
- Webhook notifications

## Authentication

All API requests require authentication using API keys. To obtain an API key:

1. Register for an account at the [Developer Portal](https://example.com/developer)
2. Create a new application in your developer dashboard
3. Generate an API key for your application
4. Include this key in all API requests

Example:

```bash
curl -X GET "https://api.legalprejudice.example.com/v1/assessments" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## API Endpoints

### Assessment Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/assessments` | GET | List all assessments |
| `/v1/assessments` | POST | Create a new assessment |
| `/v1/assessments/{id}` | GET | Get a specific assessment |
| `/v1/assessments/{id}` | PUT | Update an assessment |
| `/v1/assessments/{id}` | DELETE | Delete an assessment |
| `/v1/assessments/{id}/calculate` | POST | Calculate risk score |
| `/v1/assessments/{id}/report` | GET | Generate assessment report |

### Factor Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/factors` | GET | List all prejudice factors |
| `/v1/factors/{id}` | GET | Get a specific factor |
| `/v1/factors/categories` | GET | List factor categories |
| `/v1/factors/search` | GET | Search for factors |

### Results Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/results` | GET | List all assessment results |
| `/v1/results/{id}` | GET | Get a specific result |
| `/v1/results/statistics` | GET | Get statistical analysis |
| `/v1/results/export` | POST | Export results in various formats |

### Integration Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/integrations/cms` | POST | Push to case management system |
| `/v1/integrations/calendar` | POST | Create calendar event |
| `/v1/integrations/documents` | POST | Generate document |

### Webhook Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/webhooks` | GET | List registered webhooks |
| `/v1/webhooks` | POST | Register a new webhook |
| `/v1/webhooks/{id}` | DELETE | Delete a webhook |
| `/v1/webhooks/test` | POST | Test webhook delivery |

## Request and Response Formats

All API endpoints accept and return JSON data. The general format for responses is:

```json
{
  "status": "success",
  "data": {
    // Response data here
  },
  "meta": {
    "pagination": {
      "total": 100,
      "page": 1,
      "per_page": 10
    }
  }
}
```

Error responses follow this format:

```json
{
  "status": "error",
  "error": {
    "code": "invalid_request",
    "message": "The request was invalid",
    "details": [
      "Field 'likelihood' must be between 1 and 5"
    ]
  }
}
```

## Rate Limiting

The API implements rate limiting to ensure fair usage:

- 100 requests per minute per API key
- 5,000 requests per day per API key

Rate limit information is included in response headers:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1598356800
```

## Pagination

List endpoints support pagination using the following query parameters:

- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10, max: 100)

Example:

```
GET /v1/assessments?page=2&per_page=25
```

## Filtering and Sorting

List endpoints support filtering and sorting:

- Filtering: `?filter[field]=value`
- Sorting: `?sort=field` or `?sort=-field` (descending)

Example:

```
GET /v1/assessments?filter[risk_level]=high&sort=-created_at
```

## SDK Libraries

We provide official SDK libraries for easy integration:

- [Python SDK](https://github.com/yourusername/legal-prejudice-python)
- [JavaScript SDK](https://github.com/yourusername/legal-prejudice-js)
- [Java SDK](https://github.com/yourusername/legal-prejudice-java)
- [C# SDK](https://github.com/yourusername/legal-prejudice-csharp)

## Webhooks

Webhooks allow you to receive real-time notifications when events occur in the system. To use webhooks:

1. Register a webhook URL through the API or developer portal
2. Select the events you want to subscribe to
3. Implement an endpoint on your server to receive webhook payloads
4. Process the webhook data in your application

Example webhook payload:

```json
{
  "event": "assessment.completed",
  "created_at": "2025-08-28T18:20:45Z",
  "data": {
    "assessment_id": "asmt_12345",
    "risk_score": 18,
    "risk_level": "high",
    "factors_count": 5
  }
}
```

## Example Code

### Creating an Assessment

```python
import requests

api_key = "your_api_key"
api_url = "https://api.legalprejudice.example.com/v1"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "case_reference": "Smith v. Jones",
    "judge_name": "Hon. Robert Williams",
    "court_id": "fed_9th_circuit",
    "assessment_date": "2025-08-28",
    "factors": [
        {
            "factor_id": "relationship_financial",
            "likelihood": 4,
            "impact": 5,
            "notes": "Judge previously represented defendant's company"
        },
        {
            "factor_id": "conduct_statements",
            "likelihood": 3,
            "impact": 4,
            "notes": "Judge made disparaging remarks about plaintiff's counsel"
        }
    ]
}

response = requests.post(
    f"{api_url}/assessments",
    headers=headers,
    json=data
)

if response.status_code == 201:
    assessment = response.json()["data"]
    print(f"Assessment created with ID: {assessment['id']}")
    print(f"Risk score: {assessment['risk_score']}")
    print(f"Risk level: {assessment['risk_level']}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
```

### Retrieving Assessment Results

```javascript
const axios = require('axios');

const apiKey = 'your_api_key';
const apiUrl = 'https://api.legalprejudice.example.com/v1';

async function getAssessment(assessmentId) {
  try {
    const response = await axios.get(`${apiUrl}/assessments/${assessmentId}`, {
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });
    
    const assessment = response.data.data;
    console.log(`Assessment ID: ${assessment.id}`);
    console.log(`Risk score: ${assessment.risk_score}`);
    console.log(`Risk level: ${assessment.risk_level}`);
    console.log(`Factors: ${assessment.factors.length}`);
    
    return assessment;
  } catch (error) {
    console.error('Error retrieving assessment:', error.response?.data || error.message);
    throw error;
  }
}

getAssessment('asmt_12345');
```

## API Versioning

The API uses versioning in the URL path (e.g., `/v1/assessments`). When breaking changes are introduced, a new version will be released (e.g., `/v2/assessments`). We maintain older versions for at least 12 months after a new version is released.

## Support

If you encounter any issues or have questions about the API:

- Check the [API Status Page](https://status.legalprejudice.example.com)
- Visit the [Developer Forum](https://forum.legalprejudice.example.com)
- Contact support at api-support@legalprejudice.example.com

## Changelog

### v1.0.0 (2025-08-01)
- Initial API release

### v1.1.0 (2025-08-15)
- Added webhook functionality
- Improved error messages
- Added bulk assessment endpoint

### v1.2.0 (2025-08-28)
- Added report generation endpoints
- Enhanced filtering capabilities
- Improved rate limiting with burst allowance