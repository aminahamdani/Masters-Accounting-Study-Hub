# Local PostgreSQL Database Setup

## Quick Setup Commands

### Step 1: Connect to PostgreSQL as postgres user

```bash
psql -U postgres
```

### Step 2: Create the database

Once connected to psql, run:

```sql
CREATE DATABASE studyhub;
```

### Step 3: Exit psql

```sql
\q
```

## Complete Command Sequence

You can also do this in one line:

```bash
psql -U postgres -c "CREATE DATABASE studyhub;"
```

## Verify Database Creation

To verify the database was created:

```bash
psql -U postgres -c "\l" | findstr studyhub
```

Or connect to the new database:

```bash
psql -U postgres -d studyhub
```

## Next Steps

After creating the database:

1. Run the schema: `psql -U postgres -d studyhub -f backend/schema.sql`
2. Run seed data: `psql -U postgres -d studyhub -f backend/seed_data.sql`
3. Update your `.env` file with:
   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=postgres
   DB_PASSWORD=your-password
   DB_NAME=studyhub
   ```
