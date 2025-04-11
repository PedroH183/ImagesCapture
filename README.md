# ImagesCapture

A web scraping application that captures product information from Mercado Livre, stores it in a PostgreSQL database, and sends notifications via Telegram.

## 📋 Overview

This project uses Selenium to scrape product information from Mercado Livre (specifically searching for "Acer Predator" products by default). 

## Features

- Automated web scraping using Selenium with headless Chrome
- PostgreSQL database integration for data storage
- Telegram bot integration for real-time notifications
- Containerized setup with Docker and Docker Compose
- Dependency injection pattern for better code organization

## Tech Stack

- **Python 3.10+**
- **Selenium**: Web automation and scraping
- **PostgreSQL**: Database storage
- **Docker & Docker Compose**: Containerization
- **Python Telegram Bot**: Telegram integration
- **psycopg2**: PostgreSQL adapter for Python

## Running

1. Build and start the containers:
   ```bash
   docker-compose up -d
   ```

## Project Structure

```
ImagesCapture/
├── app.py                  # Main application entry point
├── docker-compose.yml      # Docker Compose configuration
├── dockerfile              # Docker configuration
├── infra/                  # Infrastructure code
│   └── database/           # Database connection and queries
├── makefile                # Build automation
├── requirements.txt        # Python dependencies
├── services/               # Service modules
│   ├── CaptureImages/      # Web scraping service
│   └── TelegramBot/        # Telegram notification service
└── utils/                  # Utility classes
    ├── DependencyInjector/ # Dependency injection implementation
    └── Singleton/          # Singleton pattern implementation
```
