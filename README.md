# Ayvora Platform

AI-powered global dropshipping commerce platform with a premium Next.js storefront, FastAPI backend, CRM foundation, supplier/payment/shipping integration boundaries and AI commerce services.

## Stack
- Frontend: Next.js, React, TypeScript, Tailwind CSS, Framer Motion-ready UI.
- Backend: Python, FastAPI, SQLAlchemy, PostgreSQL, Redis, Celery-ready workers.
- Commerce: catalog, product detail, admin CRM, cart/checkout foundation, SEO, analytics and integrations.
- AI: SEO generation, product opportunity scoring, recommendations/translation/image-enhancement extension points.

## Run locally
```bash
docker compose up --build
```

- Web: http://localhost:3000
- API: http://localhost:8000
- API docs: http://localhost:8000/api/docs

## Development checks
```bash
cd services/api && pip install -e .[test] && pytest app/tests
cd apps/web && npm install && npm run typecheck
```
