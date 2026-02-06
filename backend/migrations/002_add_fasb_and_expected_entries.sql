-- Add fasb_link to topics, expected_entries to practice_templates
-- Master's Accounting Study Hub

ALTER TABLE topics ADD COLUMN IF NOT EXISTS fasb_link VARCHAR(500);

-- Add expected_entries for Ledger Simulator validation (JSONB for PostgreSQL)
ALTER TABLE practice_templates ADD COLUMN IF NOT EXISTS expected_entries JSONB;
