# DatingVKBot (dating-vk-bot)

## About

### Create your personal account!

<img src="images/scr_form.jpg" height="500" title="Create account!">

### Find friends online in VK!

<img src="images/src_finding.jpg" height="500" title="Find friends!">

### Get matches!

<img src="images/scr_match.jpg" height="500" title="Match!">

### Chat with randoms anonymously!

<img src="images/scr_chat.jpg" height="500" title="Chat!">

## Developer

### Build & Run

```bash
docker compose up --build
```

### Backup

```bash
# Enter the database instance
docker exec -it dating-database bash

# Ensure backup directory exists
mkdir -p /var/lib/postgresql/data/backup

# Make a backup
pg_dump $POSTGRES_DB > /var/lib/postgresql/data/backup/"$(date '+%Y-%m-%d').sql"

# Check that backup is present
sudo ls pgdata/backup/

# Take backup away
cp pgdata/backup/"$(date '+%Y-%m-%d').sql" ./backup-"$(date '+%Y-%m-%d').sql"
```

### Restore

```bash
# Stop an application
docker compose down

# Remove all images, containers, folders
# ...

# Start and Exit the database to initialize it
docker compose up database

# Ensure backup directory exists
mkdir -p ./pgdata/backup

# Copy backup to pgdata
cp ./"$DATING_BACKUP_SQL" ./pgdata/backup/"$DATING_BACKUP_SQL"

# Start the database
docker compose up database

# Enter the database instance
docker exec -it dating-database bash

# Restore
psql < /var/lib/postgresql/data/backup/"$DATING_BACKUP_SQL"

# Restart
docker compose up --build
```
