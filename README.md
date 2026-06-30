# HarvestHelp SL: Agriculture Support System

![HarvestHelp SL UI](https://private-us-east-1.manuscdn.com/sessionFile/Tkn5x9GBoVTryYvW4MEDut/sandbox/TF3NZKssuJRzxEWh19iWlm-images_1782837157377_na1fn_L2hvbWUvdWJ1bnR1L2hhcnZlc3RoZWxwX3VpX3NjcmVlbnNob3Q.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvVGtuNXg5R0JvVlRyeVl2VzRNRUR1dC9zYW5kYm94L1RGM05aS3NzdUpSenhFV2gxOWlXbG0taW1hZ2VzXzE3ODI4MzcxNTczNzdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyaGhjblpsYzNSb1pXeHdYM1ZwWDNOamNtVmxibk5vYjNRLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=pHS5~4stQDG5eD78qDJ31OZIjpLVuFliSf~bhqULedT8VYmpT~w7FZzlKpFYIVK0o8LVHpVLxVesRERUEep1uHRIBzrqha8kcxY5N0WJFVwwpRxrpKvYFeVc9Yck3uAdzy-7NCGgHsol0jgOvIoRk6AAUUK89cA23XGcTQQVnFRZR-XSanPVAZJ1KQO0eg3bC5Q0AjHqw~PeIKwVqtF3pMsU4WoqP0xxWr7sxNi6MKzIZRM3QLBRvSXwwK22vwRapYw5yQOWL8NbXr4g-Hzw6ZMy6Crshuh4mr1pv-Qhb2bO4EsWp7d4svv49TzvMjCzeCVK0Yo3ODRXIQEiPS4MxQ__)

## Overview
**HarvestHelp SL** is a GUI-based Python application designed to support smallholder farmers in Sierra Leone. By providing clear financial and production projections, the system helps farmers make informed planting and sales decisions, reducing waste and improving household food security.

This project aligns with **SDG 2: Zero Hunger** and **SDG 8: Decent Work and Economic Growth**.

## Key Features
- **Farm Planning**: Calculate expected yield and seed requirements based on land size and crop type.
- **Financial Projections**: Estimate total production costs, potential revenue, and net profit.
- **Risk Assessment**: Classify projections into "Highly Profitable", "Profitable", or "Risk of Loss".
- **Data Accessibility**: Export farm projections to CSV for use in spreadsheets or for sharing with agriculture officers.
- **User-Friendly GUI**: A clean, modern interface built with Python's Tkinter library.

## Supported Crops
- Rice
- Cassava
- Maize

## Technical Implementation
The project follows **Structured Programming** principles:
- **Modular Design**: Separation of UI logic from calculation and formatting functions.
- **Input Validation**: Robust handling of numerical data to prevent runtime errors.
- **Constants & Dictionaries**: Centralized management of crop data and UI styling.
- **Persistent Storage**: Local CSV export using the standard `csv` library.

## Requirements
- Python 3.x
- Tkinter (usually included with standard Python installations)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HarvestHelp-SL.git
   ```
2. Navigate to the project directory:
   ```bash
   cd HarvestHelp-SL
   ```
3. Run the application:
   ```bash
   python HarvestHelp.py
   ```

## Project Context
Developed as a final project for **PROG103 - Principle of Structured Programming**.
**Examiner**: Elijah Fullah

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
