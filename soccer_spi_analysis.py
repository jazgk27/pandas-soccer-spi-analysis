#PandasAssignment Jazmin GK
import pandas as pd

def main():
    data_frame = pd.read_csv("spi_global_rankings.csv")
    print(data_frame.head()) #2. first five rows
    print(data_frame.tail()) #3. last five rows
    print(data_frame.describe()) #4. statistical info
    print(data_frame.nunique()) #5. number of nunique values
    print(data_frame[data_frame['off'] == 2.3]) #6. only rows where off = 2.3
    print(data_frame.sort_values(by='spi', ascending=True)) #7. rows sorted based on spi
    print(data_frame['def'].max()) #8. value of def
    print(data_frame['off'].min()) #9. value of off
    print(data_frame.sort_values(by='spi', ascending=False)) #10. data sorted by spi
    data_frame['def'] = data_frame['def'].replace(0.9, 1.0) #11.
    print(data_frame.head())
    with open('soccer.txt', 'w') as file: #12. new file
        file.write("Maximum value of def: {}\n".format(data_frame['def'].max())) #13. max balue of def question 8
        file.write("Minimum value of off: {}".format(data_frame['off'].min()))   #14. min value of off question 9
    with open('soccer.txt', 'r') as file: #15. txt in read mode
        print(file.read()) #16.

main()
