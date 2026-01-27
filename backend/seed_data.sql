-- Seed data for topics table
-- Master's Accounting Study Hub
-- PostgreSQL INSERT statements

INSERT INTO topics (name, oer_link, asc_reference) VALUES
('Revenue Recognition', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 606'),
('Leases', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 842'),
('Financial Instruments', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 825'),
('Inventory Valuation', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 330'),
('Property, Plant and Equipment', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 360'),
('Intangible Assets', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 350'),
('Income Taxes', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 740'),
('Earnings Per Share', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 260'),
('Consolidation', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 810'),
('Fair Value Measurement', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 820'),
('Statement of Cash Flows', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 230'),
('Accounting Changes and Error Corrections', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 250'),
('Contingencies', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 450'),
('Debt', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 470'),
('Equity', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 505'),
('Derivatives and Hedging', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 815'),
('Business Combinations', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 805'),
('Segment Reporting', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 280'),
('Interim Reporting', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 270'),
('Related Party Disclosures', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 850')
ON CONFLICT DO NOTHING;
