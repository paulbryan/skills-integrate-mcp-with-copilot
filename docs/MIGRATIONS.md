# Database migrations

This project uses SQLAlchemy for models and Alembic for migrations.

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize and run migrations (example):

```bash
alembic revision --autogenerate -m "create activities and participants"
alembic upgrade head
```

By default the app uses SQLite at `./activities.db`. You can set `DATABASE_URL` to a Postgres or other DB URL.
