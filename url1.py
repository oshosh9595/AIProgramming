import requests
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/categories/177295?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&rating=4'
response = requests.get(url)
#response.status_code
#response.text

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.select('.search-product-wrap')

result = []

for product in products:
    name = product.select_one('.name').text
    price = product.select_one('.price-value').text
    rating = product.select_one('.rating').text
    review_count = product.select_one('.rating-total-count').text

    result.append([name, price, rating, review_count])

print(result)

import pandas as pd

df = pd.DataFrame(result, columns=['제품명', '가격', '평점', '리뷰 수'])
df.to_csv('coupang_products.csv', index=False, encoding='cp949')

df=pd.read_csv('coupang_products.csv', encoding='cp949')

print(df.info())
print(df['평점']>4)

import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일에서 데이터 불러오기
df = pd.read_csv('coupang_products.csv', encoding='utf-8')

# 데이터 전처리
df['price'] = df['price'].str.replace(',', '').astype(int)
df['rating'] = df['rating'].astype(float)

# 시각화
sns.scatterplot(data=df, x='rating', y='price', s=100)
plt.title('Coupang Products')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.show()