# Soccer SPI Data Analysis with Pandas
Class project analyzing the FiveThirtyEight Soccer Power Index (SPI) global rankings dataset using pandas.

## Description
This script loads the SPI global rankings CSV file, performs exploratory data analysis, applies filtering, sorting, statistical summaries, value replacement, and generates a simple text report with key findings.

## Technologies Used
- Python 3
- pandas (for data manipulation and analysis)

## How to Run the Project
1. Download the dataset from:  
   [FiveThirtyEight SPI Global Rankings](https://projects.fivethirtyeight.com/soccer-api/club/spi_global_rankings.csv)  
   (or search for "club soccer SPI" on Kaggle)

2. Place the file `spi_global_rankings.csv` in the same folder as the script.

3. Install pandas (if not already installed):  
   pip install pandas 

4. Run the script:
   python soccer_spi_analysis.py 

## Main Features
- Displays the first and last five rows (`head()` / `tail()`)  
- Shows descriptive statistics (`describe()`)  
- Counts unique values (`nunique()`)  
- Filters rows (e.g., where `off` == 2.3)  
- Sorts data by SPI (ascending and descending)  
- Finds max value of `def` and min value of `off`  
- Replaces specific values (e.g., 0.9 → 1.0 in `def`)  
- Writes key results (max `def`, min `off`) to `soccer.txt` file  

## Skills Demonstrated
- Loading and exploring datasets with pandas  
- Data filtering, sorting, and transformation  
- Basic statistical operations  
- File input/output (writing and reading TXT files)

Class assignment from the Associate in Science in Computer Programming program – Palm Beach State College.

Feedback and suggestions are welcome!
