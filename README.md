# CRUD Two App

A modern full-stack CRUD application showcasing **NextJS/TypeScript** frontend and **Python FastAPI** backend development within a containerized VS Code DevContainer environment.

## 📚 Table of Contents

- [Overview](#overview)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development](#development)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [License](#license)

## Overview

This project demonstrates a professional full-stack development setup using:

- **Frontend**: NextJS 15.5 with React 19, TypeScript, and TailwindCSS v4
- **Backend**: Python FastAPI with Pydantic validation and Uvicorn server
- **Infrastructure**: Docker-based DevContainer with PostgreSQL, Redis, and various developer tools

## Technology Stack

### Frontend (`/ui`)

| Technology  | Version | Purpose                        |
| ----------- | ------- | ------------------------------ |
| NextJS      | 15.5.2  | React framework with Turbopack |
| React       | 19.1.0  | UI component library           |
| TypeScript  | ^5      | Type-safe JavaScript           |
| TailwindCSS | ^4      | Utility-first CSS framework    |
| ESLint      | ^9      | Code linting                   |

### Backend (`/api`)

| Technology | Version | Purpose                        |
| ---------- | ------- | ------------------------------ |
| Python     | 3.12    | Runtime environment            |
| FastAPI    | latest  | High-performance API framework |
| Pydantic   | latest  | Data validation                |
| Uvicorn    | latest  | ASGI server                    |
| Redis      | latest  | Caching & sessions             |
| Loguru     | latest  | Logging                        |

### DevContainer & Infrastructure

| Tool                 | Purpose                         |
| -------------------- | ------------------------------- |
| Docker Compose       | Container orchestration         |
| PostgreSQL 13        | Database (via client)           |
| AWS CLI              | Cloud services integration      |
| Dapr                 | Distributed application runtime |
| Protobuf             | API serialization               |
| LocalStack           | AWS local emulation             |
| Cypress & Playwright | E2E testing                     |

## Project Structure

```
crud-two-app/
├── .devcontainer/          # DevContainer configuration
│   ├── devcontainer.json   # VS Code container settings
│   ├── docker-compose.yml  # Docker services definition
│   ├── Dockerfile          # Python 3.12 container image
│   ├── postCreateCommand.sh # Post-setup automation
│   ├── requirements.txt    # Python dependencies
│   └── init/
│       └── init.sql        # Database initialization
├── .vscode/
│   ├── extensions.json     # Recommended extensions
│   └── launch.json         # Debug configurations
├── api/                    # Backend (FastAPI)
│   └── main.py             # API entry point
├── ui/                     # Frontend (NextJS)
│   ├── app/
│   │   ├── page.tsx        # Main page component
│   │   ├── layout.tsx      # Root layout
│   │   └── globals.css     # Global styles
│   ├── package.json        # Node dependencies
│   ├── tsconfig.json       # TypeScript config
│   └── next.config.ts      # NextJS configuration
├── ANALYSIS.md             # Technical analysis document
└── README.md               # This file
```

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Quick Start

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd crud-two-app
   ```

2. **Open in VS Code**

   ```bash
   code .
   ```

3. **Reopen in Container**
   - Press `F1` → "Dev Containers: Reopen in Container"
   - Wait for container build and dependency installation

4. **Start Backend Server**

   ```bash
   cd api
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Start Frontend Server**

   ```bash
   cd ui
   npm run dev
   ```

6. **Access Applications**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Development

### Debug Configurations (VS Code)

The project includes pre-configured debug configurations in `.vscode/launch.json`:

| Configuration              | Description                        |
| -------------------------- | ---------------------------------- |
| Python: FastAPI            | Debug backend with auto-reload     |
| Launch Chrome              | Debug frontend in Chrome           |
| Launch Firefox             | Debug frontend in Firefox          |
| Next.js: debug server-side | Debug NextJS server-side code      |
| Next.js: debug client-side | Debug NextJS client-side in Chrome |
| Next.js: debug full stack  | Full-stack debugging               |

### Running Tests

```bash
# Frontend
cd ui && npm run lint

# Backend (if tests available)
cd api && pytest
```

## API Endpoints

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| `GET`  | `/`                | Health check / Welcome message |
| `GET`  | `/items/{item_id}` | Retrieve item by ID            |
| `POST` | `/items/`          | Create new item                |

### Item Schema

```json
{
  "name": "string (required)",
  "description": "string | null",
  "price": "float (required)",
  "tax": "float | null"
}
```

## Configuration

### Environment Variables (`.devcontainer/.env`)

| Variable            | Description       |
| ------------------- | ----------------- |
| `POSTGRES_DB`       | Database name     |
| `POSTGRES_USER`     | Database user     |
| `POSTGRES_PASSWORD` | Database password |
| `POSTGRES_HOSTNAME` | Database host     |

### Forwarded Ports

| Port  | Service             |
| ----- | ------------------- |
| 5432  | PostgreSQL          |
| 5672  | RabbitMQ            |
| 6379  | Redis               |
| 8000  | FastAPI Backend     |
| 9000  | Additional services |
| 15672 | RabbitMQ Management |

## Documentation

- [**ANALYSIS.md**](./ANALYSIS.md) - In-depth technical analysis of architecture, design patterns, and best practices

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.

---

**Built with ❤️ using DevContainers, FastAPI, and NextJS**
