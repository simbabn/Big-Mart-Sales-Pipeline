# Big-Mart-Sales-Pipeline


# Data Cleaning and Export Project

This project automates the cleaning of a dataset by filling missing values in specific columns (`Outlet_Size` and `Item_Weight`) and exporting the cleaned dataset to a CSV file.

## Table of Contents
- [Big-Mart-Sales-Pipeline](#big-mart-sales-pipeline)
- [Data Cleaning and Export Project](#data-cleaning-and-export-project)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Installation](#installation)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Set Up a Virtual Environment](#step-2-set-up-a-virtual-environment)
    - [Step 3: Install Dependencies](#step-3-install-dependencies)
  - [Usage](#usage)
    - [Example](#example)
  - [Functions](#functions)
    - [clean\_data()](#clean_data)
    - [export\_to\_csv(df)](#export_to_csvdf)
  - [Contributing](#contributing)
  - [License](#license)

## Project Overview

The purpose of this project is to automate the data cleaning process by:
1. Filling missing values in the `Outlet_Size` column with random values chosen from the available sizes (`'Medium'`, `'High'`, `'Small'`) for the corresponding `Item_Type`.
2. Filling missing values in the `Item_Weight` column by generating random values between the minimum and maximum values for each group of `Outlet_Size` and `Item_Type`.
3. Exporting the cleaned dataset to a new CSV file.

## Installation

### Step 1: Clone the Repository

First, clone this repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up a Virtual Environment

It’s a good practice to use a virtual environment to isolate your project dependencies. You can create a virtual environment using `venv` as follows:

```bash
# For Windows
python -m venv venv
.venvScriptsactivate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

This will create and activate a virtual environment called `venv`.

### Step 3: Install Dependencies

Once your virtual environment is activated, you can install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries like `pandas` and `numpy`.

## Usage

1. Place your dataset in the `data/` directory and name it `data.csv` (or adjust the file path in the code if needed).
2. Run the `clean_data()` function to clean the dataset.
3. The cleaned dataset will be saved as `result.csv` in the `data/` directory.

### Example

To run the cleaning and export process, use the following Python code:

```python
from your_script import clean_data, export_to_csv

# Clean the data and export it to a CSV file
cleaned_data = clean_data()
export_to_csv(cleaned_data)
```

This will process the `data.csv` file and output the cleaned data to `result.csv`.

## Functions

### clean_data()

- **Description**: This function reads the dataset, cleans the `Outlet_Size` and `Item_Weight` columns by filling in missing values, and returns the cleaned DataFrame.
- **Process**:
  - Missing values in `Outlet_Size` are filled with random values from the available sizes for each `Item_Type`.
  - Missing values in `Item_Weight` are filled with random values between the minimum and maximum weights for each group of `Outlet_Size` and `Item_Type`.

### export_to_csv(df)

- **Description**: This function exports the cleaned DataFrame to a CSV file named `result.csv` in the `data/` directory.
- **Parameters**:
  - `df`: The cleaned DataFrame to export.

## Contributing

If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
