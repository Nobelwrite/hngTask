# INFO API

This is a public API developed for the HNG12 Stage 0 Backend task using Django. It provides basic information such as your email, the current date and time in ISO 8601 format, and the GitHub URL of this repository.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Nobelwrite/info_api.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations to set up the database:

```bash
python manage.py migrate
```
4. Run the API locally:

```bash
python manage.py runserver
```

## API Documentation

### Endpoint

**GET** `/info/get_info`

### Response

```json
{
  "email": "damilolajoseph91@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Nobelwrite/hng12-stage0-info-api"
}
```

### Backlinks

- [Python Developers](https://hng.tech/hire/python-developers)