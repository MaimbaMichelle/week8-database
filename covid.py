import pandas as pd
import matplotlib.pyplot as plt

# Example of loading and cleaning the data
def load_data():
    # Load the COVID-19 data (you would replace this with actual data from OWID)
    data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhucsse/confirmed_global.csv')
    return data

def plot_data(data):
    # Simple example of plotting confirmed cases for a country
    country_data = data[data['location'] == 'Kenya']
    plt.plot(country_data['date'], country_data['total'])
    plt.title('COVID-19 Total Confirmed Cases in Kenya')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.show()

# Main function
def main():
    data = load_data()
    plot_data(data)

if __name__ == "__main__":
    main()
