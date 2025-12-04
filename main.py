import pandas as pd
import re

df = pd.read_json('orders_simple.json')


def clean_amount(amount:str)->float:
    amount = amount.strip('$')
    amount = float(amount)
    return amount

def clean_ints(days:str)->int:
    days = int(days)
    return days

def clean_rating(rating:str)->float:
    rating = float(rating)
    return rating

def clean_html(html:str)->str:
    cleaned = re.sub("<.*?>", " ", html)
    return cleaned

def clean_coupon(coupon:str) ->str:
    if coupon == "":
        coupon = "no coupon"
    return coupon

def convert_country(country):
    country = str(country)
    return country
    

df['total_amount'] = df['total_amount'].apply(clean_amount)
df['shipping_days'] = df['shipping_days'].apply(clean_ints)
df['customer_age'] = df['customer_age'].apply(clean_ints)
df['rating'] = df['rating'].apply(clean_rating)
df['order_date'] = pd.to_datetime(df['order_date'])
df['items_html'] =  df['items_html'].apply(clean_html)
df['coupon_used'] = df['coupon_used'].apply(clean_coupon)
df['order_month'] = df['order_date'].dt.month
df['high_value_order'] = df['total_amount'] > df['total_amount'].mean()
df['avg_rating_country'] = df.groupby('country')['rating'].mean()

 


df.to_csv('clean_orders_347662413.csv')