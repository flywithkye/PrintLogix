DROP TABLE IF EXISTS `genralrecords`  ;
     CREATE TABLE genralrecords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                printerModel TEXT,
                employee_name INTEGER,
                quantity INTEGER,
                color TEXT,
                paper_size TEXT,
                date TEXT,
                time TEXT,
                paper_type TEXT,
                comments TEXT,
                description TEXT);

INSERT INTO genralrecords (printerModel, employee_name, quantity, color, paper_size, date, time, paper_type, comments, description)
VALUES
('PrinterA', 'John Doe', 50, 'Black', 'A4', '2023-11-28', '09:00 AM', 'Standard', 'No comments', 'Printing documents for meeting'),
('PrinterB', 'Jane Smith', 30, 'Color', 'Letter', '2023-11-28', '10:30 AM', 'Glossy', 'Printed marketing materials', 'Promotional flyers for event'),
('PrinterC', 'Bob Johnson', 20, 'Black', 'Legal', '2023-11-29', '02:45 PM', 'Recycled', 'Urgent printing', 'Legal documents for client'),
('PrinterA', 'Alice Williams', 15, 'Color', 'A3', '2023-11-29', '04:15 PM', 'Matte', 'Printed photos', 'Personal photo prints'),
('PrinterB', 'Charlie Brown', 40, 'Black', 'A4', '2023-11-30', '11:20 AM', 'Standard', 'Meeting handouts', 'Documents for team presentation');

