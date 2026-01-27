# Master's Accounting Study Hub

A comprehensive study platform for Master's level accounting students, featuring topic search, practice templates, and progress tracking.

## 🚀 Features

- **Topic Search**: Search accounting topics by name with case-insensitive matching
- **Practice Templates**: Practice problems and templates for various accounting topics
- **Progress Tracking**: Track your study progress across different topics
- **RESTful API**: FastAPI-based backend with automatic API documentation
- **PostgreSQL Database**: Robust database schema with proper indexing and relationships

## 📋 Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (Azure PostgreSQL for production)
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

## 🏗️ Project Structure

```
Masters Accounting Study Hub/
├── backend/                 # FastAPI backend application
│   ├── main.py             # Application entry point
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database connection and session management
│   ├── requirements.txt    # Python dependencies
│   ├── development.md      # Development setup guide
│   ├── core/               # Core application components
│   │   └── app.py          # Application factory
│   ├── routers/            # API route handlers
│   │   ├── health.py       # Health check endpoint
│   │   ├── search.py       # Search functionality
│   │   ├── practice.py     # Practice templates
│   │   └── progress.py     # Progress tracking
│   ├── models/             # SQLAlchemy database models
│   ├── schemas/            # Pydantic schemas
│   └── migrations/         # Database migration files
├── infrastructure/         # Infrastructure as code
│   ├── schema.sql          # Database schema
│   └── seed_data.sql       # Seed data for development
└── README.md               # This file
```

## 🚦 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL (local or Azure)
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Masters Accounting Study Hub"
   ```

2. **Set up the backend**
   ```bash
   cd backend
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment (Windows)
   .venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Copy example file
   copy .env.example .env
   
   # Edit .env with your database credentials
   ```

4. **Set up the database**
   ```bash
   # Create database
   psql -U postgres
   CREATE DATABASE studyhub;
   \q
   
   # Run schema
   psql -U postgres -d studyhub -f ../infrastructure/schema.sql
   
   # Load seed data
   psql -U postgres -d studyhub -f ../infrastructure/seed_data.sql
   ```

5. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - API Root: http://localhost:8000
   - Health Check: http://localhost:8000/health
   - API Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## 📚 API Endpoints

### Health Check
- `GET /health` - Check API health status

### Search
- `GET /api/search?q={query}` - Search topics by name

### Practice (Coming Soon)
- Practice template endpoints

### Progress (Coming Soon)
- Progress tracking endpoints

## 🗄️ Database Schema

The database includes three main tables:

- **topics**: Accounting study topics with OER links and ASC references
- **practice_templates**: Practice problem templates linked to topics
- **progress_logs**: User progress tracking for topics

See `infrastructure/schema.sql` for the complete schema definition.

## 🔧 Development

For detailed development setup instructions, see [backend/development.md](backend/development.md).

### Key Features

- **Modular Architecture**: Separated concerns with routers, models, and schemas
- **Lazy Database Initialization**: Server can start without immediate database connection
- **Auto-reload**: Development server automatically reloads on code changes
- **Type Safety**: Pydantic schemas for request/response validation

## 🚀 Deployment

### Azure App Service

1. Set environment variables in Azure Portal
2. Configure Azure PostgreSQL firewall rules
3. Deploy using Azure CLI or GitHub Actions

See `backend/development.md` for detailed deployment instructions.

## 📝 License

[Add your license here]

## 🤝 Contributing

[Add contribution guidelines here]

## 📧 Contact

[Add contact information here]
