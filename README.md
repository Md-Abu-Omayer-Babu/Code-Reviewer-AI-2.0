# Code Reviewer AI

A full-stack application with a Next.js frontend and FastAPI backend for code analysis and review.

## Project Structure

This project consists of two main components:

- **Frontend**: A Next.js application with React 19 and Tailwind CSS
- **Backend**: A FastAPI application with MongoDB for data storage

## Getting Started

### Frontend

First, navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

Then run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Backend

Navigate to the backend directory and install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000)

## Features

- User authentication (login/register)
- Code analysis tools:
  - Class finder
  - Function finder
  - Comment finder
  - File operations
- MongoDB integration for data persistence

## API Documentation

Once the backend server is running, you can access the interactive API documentation at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Learn More

### Frontend

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [React Documentation](https://react.dev/) - learn about React

### Backend

- [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI
- [MongoDB Documentation](https://docs.mongodb.com/) - learn about MongoDB

## Deployment

### Frontend

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

### Backend

For the backend, you can deploy using Docker containers on platforms like:
- [Heroku](https://www.heroku.com/)
- [DigitalOcean](https://www.digitalocean.com/)
- [AWS](https://aws.amazon.com/)
- [Azure](https://azure.microsoft.com/)
