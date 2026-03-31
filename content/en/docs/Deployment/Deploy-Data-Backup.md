---
title: "Data Backup Strategy"
linkTitle: "Data Backup"
weight: 30
description:
  "Guidelines for backing up and restoring SW360 data across container and bare metal deployments."
---

Regular backups are critical for maintaining the integrity and availability of
your SW360 instance. Given the importance of compliance data, a robust backup
strategy ensures that you can recover from hardware failures, data corruption,
or accidental deletions.

## Backup Frequency & Retention Policy

For production environments, the following retention policy is recommended as a
baseline:

| Backup Type | Frequency | Retention Period |
| :--- | :--- | :--- |
| **High-Frequency** | Every 24 hours | 14 days |
| **Long-Term** | Every 30 days | 1 year |

## Recommended: Offline Backups

For SW360 v20+, **offline backups** are the recommended method for ensuring
maximum data consistency. This involves briefly stopping the services to capture
a point-in-time snapshot of the underlying databases and configuration files.

> [!NOTE]
> Advanced administrators may choose online backup methods (e.g., CouchDB
> replication or filesystem-level snapshots like LVM/ZFS) to minimize downtime,
> but offline backups are the most reliable starting point.

---

## Container Deployments

In a standard `docker-compose` setup, all persistent data is stored in Docker
volumes. 

### 1. Backing Up Docker Volumes

To perform a consistent backup, stop the stack and use a temporary container to
tarball the volumes:

1. **Stop the SW360 stack**:
    ```bash
    docker compose stop
    ```

2. **Back up the volumes**:
    Use a temporary container to create compressed tarballs of the `couchdb`,
    `postgres_storage`, and `etc` volumes.
    ```bash
    # Backup CouchDB
    docker run --rm -v couchdb:/data -v $(pwd)/backups:/backup alpine tar czf /backup/sw360_couchdb_$(date +%F).tar.gz -C /data .

    # Backup PostgreSQL (Keycloak)
    docker run --rm -v postgres_storage:/data -v $(pwd)/backups:/backup alpine tar czf /backup/sw360_postgres_$(date +%F).tar.gz -C /data .

    # Backup SW360 Configuration
    docker run --rm -v etc:/data -v $(pwd)/backups:/backup alpine tar czf /backup/sw360_etc_$(date +%F).tar.gz -C /data .
    ```

3. **Restart the services**:
    ```bash
    docker compose start
    ```

### 2. Restoring Docker Volumes

To restore data to a new environment:

1. **Recreate the volumes**:
    ```bash
    docker volume create couchdb
    docker volume create postgres_storage
    docker volume create etc
    ```

2. **Extract the backups**:
    ```bash
    docker run --rm -v couchdb:/data -v $(pwd)/backups:/backup alpine sh -c "tar xzf /backup/sw360_couchdb_*.tar.gz -C /data"
    docker run --rm -v postgres_storage:/data -v $(pwd)/backups:/backup alpine sh -c "tar xzf /backup/sw360_postgres_*.tar.gz -C /data"
    docker run --rm -v etc:/data -v $(pwd)/backups:/backup alpine sh -c "tar xzf /backup/sw360_etc_*.tar.gz -C /data"
    ```

---

## Bare Metal Deployments

On bare metal, backups focus on the service-specific data directories and
configuration paths.

### 1. PostgreSQL Database (Keycloak)
While `pg_dump` is often used for online backups, performing a file-level backup
of the data directory during maintenance ensures a full snapshot of the cluster
state.

```bash
# Stop the service
sudo systemctl stop postgresql

# Backup the data directory (typically /var/lib/postgresql/data)
sudo tar -czf sw360_postgres_$(date +%F).tar.gz /var/lib/postgresql/data

# Restart the service
sudo systemctl start postgresql
```

### 2. CouchDB Database
For CouchDB 3.5, backing up the primary data is sufficient. The search indexes
(Nouveau) do not need to be backed up as they can be reconstructed from the
primary data.

```bash
# Stop CouchDB
sudo systemctl stop couchdb

# Backup the data directory
sudo tar -czf sw360_couchdb_$(date +%F).tar.gz /opt/couchdb/data

# Restart CouchDB
sudo systemctl start couchdb
```

---

## File System & Configuration

Beyond the databases, ensure that the following file system paths are included
in your backup routine:

| Path | Description |
| :--- | :--- |
| `/etc/sw360` | SW360 Runtime configuration and `sw360.properties` |
| `/var/lib/sw360/attachments` | Attachment store (if filesystem storage is enabled) |
| `/path/to/deployment/.env` | Environment files used for container orchestration |

### Example Backup Command
```bash
sudo tar -czf sw360_config_attachments_$(date +%F).tar.gz /etc/sw360 /var/lib/sw360/attachments
```

## Restoration Checklist
When restoring from a backup, always verify the following:
- [ ] User and Group permissions are preserved (e.g., `chown -R couchdb:couchdb`
  for CouchDB data).
- [ ] OIDC Client Secrets in the restored database match the configuration in
  `.env` or `sw360.properties`.
- [ ] Network connectivity between the Application Server and the Database Server
  is verified.
- [ ] The SW360 Backend logs are monitored for any initialization errors
  post-restore.
