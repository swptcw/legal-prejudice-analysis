# Docker Deployment for Legal Prejudice Analysis Project

This directory contains all the necessary Docker configuration files to deploy the complete Legal Prejudice Analysis system, including the web calculator, API server, and supporting services.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (version 20.10.0 or higher)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 2.0.0 or higher)
- At least 2GB of available RAM
- At least 1GB of free disk space

## Quick Start

To deploy the entire system with a single command:

```bash
docker-compose up -d
```

This will:
1. Pull or build all required Docker images
2. Create necessary networks and volumes
3. Start all services in the correct order
4. Configure the system for immediate use

Once deployed, you can access:
- Web Calculator: http://localhost:8080
- API Documentation: http://localhost:8080/api/docs
- Admin Interface: http://localhost:8080/admin (default credentials in .env file)

## Configuration

### Environment Variables

Copy the example environment file and modify as needed:

```bash
cp .env.example .env
```

Edit the `.env` file to configure:
- Database credentials
- API keys and secrets
- External service connections
- Feature toggles
- Logging levels

### Volumes

The following Docker volumes are created to persist data:

- `legal_prejudice_db_data`: Database storage
- `legal_prejudice_uploads`: User uploaded files
- `legal_prejudice_logs`: Application logs

## Component Services

### Web Frontend

The web calculator and user interface:
- Image: `legal-prejudice/web-frontend`
- Ports: 80 (internal)
- Environment variables: See `web-frontend.env.example`

### API Server

The backend API service:
- Image: `legal-prejudice/api-server`
- Ports: 5000 (internal)
- Environment variables: See `api-server.env.example`
- Healthcheck: `/health` endpoint

### Database

PostgreSQL database for storing assessment data:
- Image: `postgres:14-alpine`
- Ports: 5432 (internal)
- Environment variables: See `database.env.example`
- Volumes: `legal_prejudice_db_data`

### Nginx

Reverse proxy for routing and SSL termination:
- Image: `nginx:alpine`
- Ports: 8080:80 (external:internal)
- Configuration: `./nginx/conf.d/`

## Scaling and Production Use

For production deployments, consider:

1. **SSL Configuration**:
   - Place SSL certificates in `./nginx/certs/`
   - Update `nginx/conf.d/default.conf` to enable HTTPS

2. **Database Backup**:
   - Use the provided backup script: `./scripts/backup-db.sh`
   - Configure automated backups in your environment

3. **Horizontal Scaling**:
   - API servers can be scaled with `docker-compose up -d --scale api-server=3`
   - Ensure database is properly configured for multiple connections

4. **Monitoring**:
   - Prometheus metrics available at `/metrics` endpoint
   - Sample Grafana dashboards in `./monitoring/dashboards/`

## Troubleshooting

### Viewing Logs

```bash
# View logs for all services
docker-compose logs

# View logs for a specific service
docker-compose logs api-server

# Follow logs in real-time
docker-compose logs -f
```

### Common Issues

1. **Database Connection Errors**:
   - Check database credentials in `.env` file
   - Ensure database service is running: `docker-compose ps`

2. **Web Interface Not Loading**:
   - Check nginx logs: `docker-compose logs nginx`
   - Verify web-frontend is running: `docker-compose ps web-frontend`

3. **API Errors**:
   - Check API server logs: `docker-compose logs api-server`
   - Verify database migrations have run successfully

### Resetting the Environment

To completely reset the environment (will delete all data):

```bash
docker-compose down -v
docker-compose up -d
```

## Updating

To update to the latest version:

```bash
git pull
docker-compose down
docker-compose pull
docker-compose up -d
```

For major version upgrades, please refer to the migration guide in the documentation.

## Security Considerations

- Default credentials are for development only
- Change all passwords in production
- Consider using Docker secrets for sensitive information
- Review and adjust file permissions as needed
- Enable SSL for all production deployments