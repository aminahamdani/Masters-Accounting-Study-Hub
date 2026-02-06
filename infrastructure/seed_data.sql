-- Seed data for Master's Accounting Study Hub
-- Topics with OER links, ASC references, and FASB Codification (Basic View) links
-- PostgreSQL

INSERT INTO topics (name, oer_link, asc_reference, fasb_link) VALUES
('Revenue Recognition', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 606', 'https://asc.fasb.org/Search/Results?q=606'),
('Leases', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 842', 'https://asc.fasb.org/Search/Results?q=842'),
('Financial Instruments', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 825', 'https://asc.fasb.org/Search/Results?q=825'),
('Inventory Valuation', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 330', 'https://asc.fasb.org/Search/Results?q=330'),
('Property, Plant and Equipment', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 360', 'https://asc.fasb.org/Search/Results?q=360'),
('Intangible Assets', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 350', 'https://asc.fasb.org/Search/Results?q=350'),
('Income Taxes', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 740', 'https://asc.fasb.org/Search/Results?q=740'),
('Earnings Per Share', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 260', 'https://asc.fasb.org/Search/Results?q=260'),
('Consolidation', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 810', 'https://asc.fasb.org/Search/Results?q=810'),
('Fair Value Measurement', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 820', 'https://asc.fasb.org/Search/Results?q=820'),
('Statement of Cash Flows', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 230', 'https://asc.fasb.org/Search/Results?q=230'),
('Accounting Changes and Error Corrections', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 250', 'https://asc.fasb.org/Search/Results?q=250'),
('Contingencies', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 450', 'https://asc.fasb.org/Search/Results?q=450'),
('Debt', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 470', 'https://asc.fasb.org/Search/Results?q=470'),
('Equity', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 505', 'https://asc.fasb.org/Search/Results?q=505'),
('Derivatives and Hedging', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 815', 'https://asc.fasb.org/Search/Results?q=815'),
('Business Combinations', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 805', 'https://asc.fasb.org/Search/Results?q=805'),
('Segment Reporting', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 280', 'https://asc.fasb.org/Search/Results?q=280'),
('Interim Reporting', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 270', 'https://asc.fasb.org/Search/Results?q=270'),
('Related Party Disclosures', 'https://www.openstax.org/details/books/principles-financial-accounting', 'ASC 850', 'https://asc.fasb.org/Search/Results?q=850')
;

-- Update existing topics (run after initial schema if topics already exist) with FASB links if they were inserted without them
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=606' WHERE asc_reference = 'ASC 606' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=842' WHERE asc_reference = 'ASC 842' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=825' WHERE asc_reference = 'ASC 825' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=330' WHERE asc_reference = 'ASC 330' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=360' WHERE asc_reference = 'ASC 360' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=350' WHERE asc_reference = 'ASC 350' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=740' WHERE asc_reference = 'ASC 740' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=260' WHERE asc_reference = 'ASC 260' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=810' WHERE asc_reference = 'ASC 810' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=820' WHERE asc_reference = 'ASC 820' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=230' WHERE asc_reference = 'ASC 230' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=250' WHERE asc_reference = 'ASC 250' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=450' WHERE asc_reference = 'ASC 450' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=470' WHERE asc_reference = 'ASC 470' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=505' WHERE asc_reference = 'ASC 505' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=815' WHERE asc_reference = 'ASC 815' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=805' WHERE asc_reference = 'ASC 805' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=280' WHERE asc_reference = 'ASC 280' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=270' WHERE asc_reference = 'ASC 270' AND (fasb_link IS NULL OR fasb_link = '');
UPDATE topics SET fasb_link = 'https://asc.fasb.org/Search/Results?q=850' WHERE asc_reference = 'ASC 850' AND (fasb_link IS NULL OR fasb_link = '');

-- Practice templates (10–15 scenarios) with expected journal entries for Ledger Simulator
-- topic_id 1 = Revenue Recognition, 2 = Leases, 3 = Financial Instruments, 4 = Inventory, 5 = PP&E, etc.

INSERT INTO practice_templates (topic_id, template_text, expected_entries) VALUES
(1, 'Company sells goods for $5,000 on account. Record the journal entry for revenue recognition.', '[{"account":"Accounts Receivable","debit":5000,"credit":0},{"account":"Sales Revenue","debit":0,"credit":5000}]'),
(1, 'Company performs services for $3,200 and receives cash. Record the entry.', '[{"account":"Cash","debit":3200,"credit":0},{"account":"Service Revenue","debit":0,"credit":3200}]'),
(2, 'Lessee records a lease liability and right-of-use asset at commencement: PV of payments $100,000. Record the initial lease entry.', '[{"account":"Right-of-Use Asset","debit":100000,"credit":0},{"account":"Lease Liability","debit":0,"credit":100000}]'),
(3, 'Company purchases trading securities for $15,000 cash. Record the investment.', '[{"account":"Trading Securities","debit":15000,"credit":0},{"account":"Cash","debit":0,"credit":15000}]'),
(4, 'Company purchases inventory on account for $8,000. Record the purchase.', '[{"account":"Inventory","debit":8000,"credit":0},{"account":"Accounts Payable","debit":0,"credit":8000}]'),
(4, 'Company sells inventory that cost $4,000 for $6,500 cash. Record the sale and cost of goods sold.', '[{"account":"Cash","debit":6500,"credit":0},{"account":"Sales Revenue","debit":0,"credit":6500},{"account":"Cost of Goods Sold","debit":4000,"credit":0},{"account":"Inventory","debit":0,"credit":4000}]'),
(5, 'Company purchases equipment for $25,000 cash. Record the acquisition.', '[{"account":"Equipment","debit":25000,"credit":0},{"account":"Cash","debit":0,"credit":25000}]'),
(5, 'Record depreciation expense of $2,500 for the period on equipment.', '[{"account":"Depreciation Expense","debit":2500,"credit":0},{"account":"Accumulated Depreciation—Equipment","debit":0,"credit":2500}]'),
(6, 'Company recognizes amortization of $1,200 on a finite-life intangible asset.', '[{"account":"Amortization Expense","debit":1200,"credit":0},{"account":"Accumulated Amortization","debit":0,"credit":1200}]'),
(7, 'Company records income tax expense of $12,000 and deferred tax liability increase of $2,000. Record the tax entry.', '[{"account":"Income Tax Expense","debit":12000,"credit":0},{"account":"Income Tax Payable","debit":0,"credit":10000},{"account":"Deferred Tax Liability","debit":0,"credit":2000}]'),
(8, 'Company declares and pays a cash dividend of $0.50 per share on 100,000 shares. Record the declaration and payment.', '[{"account":"Retained Earnings","debit":50000,"credit":0},{"account":"Dividends Payable","debit":0,"credit":50000},{"account":"Dividends Payable","debit":50000,"credit":0},{"account":"Cash","debit":0,"credit":50000}]'),
(10, 'Company records an unrealized gain of $800 on investments measured at fair value through OCI.', '[{"account":"Fair Value Adjustment—OCI","debit":800,"credit":0},{"account":"Accumulated Other Comprehensive Income","debit":0,"credit":800}]'),
(11, 'Company borrows $50,000 from a bank. Record the loan proceeds.', '[{"account":"Cash","debit":50000,"credit":0},{"account":"Notes Payable","debit":0,"credit":50000}]'),
(11, 'Operating activities: Cash received from customers $45,000; paid to suppliers $28,000. Net cash from operations? (Record summary entry for cash from customers.)', '[{"account":"Cash","debit":45000,"credit":0},{"account":"Accounts Receivable","debit":0,"credit":45000}]'),
(14, 'Company issues $100,000 face value bonds at 98. Record the bond issuance.', '[{"account":"Cash","debit":98000,"credit":0},{"account":"Discount on Bonds Payable","debit":2000,"credit":0},{"account":"Bonds Payable","debit":0,"credit":100000}]')
;
