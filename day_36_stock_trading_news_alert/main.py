import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "D0T7Z504M2B22M5E"
API_NEWS_KEY = "c05e9686edc04c62b6b3e43dcc259f91"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]--------------------------------------------------------------------
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]

yesterday_closing_price = data_list[0]["4. close"]

print(f"yesterday_closing_price is {yesterday_closing_price}")


#  2. - Get the day before yesterday's closing stock price------------------------------------------------------------

day_before_yesterday_data = data_list[1]
day_before_closing_price = day_before_yesterday_data["4. close"]
print(f"day_before_yesterday_closing_price is {day_before_closing_price}")


# 3. Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
print(difference)

# 4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_precent = (difference / float(yesterday_closing_price)) * 100
print(f"difference is {diff_precent} precent")

# 5. If TODO4 percentage is greater than 0.1 then print("Get News"). Instead of printing ("Get News"),--------------------
# use the News API to get articles related to the COMPANY_NAME.


if diff_precent > 0.1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_NEWS_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    articles= news_response.json()["articles"]

# 6.Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# 7. Use Python slice operator to create a list that contains the first 3 articles. Hint:-----------------------------
#  https://stackoverflow.com/questions/509211/understanding-slice-notation

first_three_articles=articles[:3]

# 8. - Create a new list of the first 3 article's headline and description using list comprehension.

artiles_first_three= [f"headline: {article['title']}. \n Brief: {article['description']}"for article in first_three_articles]

print(artiles_first_three)