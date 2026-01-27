-- Initial database schema migration
-- Master's Accounting Study Hub
-- PostgreSQL syntax

-- Create topics table
CREATE TABLE IF NOT EXISTS topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    oer_link VARCHAR(500),
    asc_reference VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index on topic name for faster searches
CREATE INDEX IF NOT EXISTS idx_topics_name ON topics(name);
CREATE INDEX IF NOT EXISTS idx_topics_asc_reference ON topics(asc_reference);

-- Create practice_templates table
CREATE TABLE IF NOT EXISTS practice_templates (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER NOT NULL,
    template_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_practice_templates_topic
        FOREIGN KEY (topic_id)
        REFERENCES topics(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create indexes on practice_templates
CREATE INDEX IF NOT EXISTS idx_practice_templates_topic_id ON practice_templates(topic_id);
CREATE INDEX IF NOT EXISTS idx_practice_templates_created_at ON practice_templates(created_at);

-- Create progress_logs table
CREATE TABLE IF NOT EXISTS progress_logs (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    topic_id INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) NOT NULL,
    notes TEXT,
    CONSTRAINT fk_progress_logs_topic
        FOREIGN KEY (topic_id)
        REFERENCES topics(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create indexes on progress_logs
CREATE INDEX IF NOT EXISTS idx_progress_logs_user_id ON progress_logs(user_id);
CREATE INDEX IF NOT EXISTS idx_progress_logs_topic_id ON progress_logs(topic_id);
CREATE INDEX IF NOT EXISTS idx_progress_logs_timestamp ON progress_logs(timestamp);
CREATE INDEX IF NOT EXISTS idx_progress_logs_status ON progress_logs(status);
CREATE INDEX IF NOT EXISTS idx_progress_logs_user_topic ON progress_logs(user_id, topic_id);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers to automatically update updated_at
CREATE TRIGGER update_topics_updated_at
    BEFORE UPDATE ON topics
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_practice_templates_updated_at
    BEFORE UPDATE ON practice_templates
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
