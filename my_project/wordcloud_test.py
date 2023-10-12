import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 텍스트 데이터를 입력하세요
text = "파이썬 워드클라우드 예제를 만들어 봅시다. 파이썬으로 텍스트 데이터를 처리하고 시각화합니다."

# 워드 클라우드 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 워드 클라우드를 화면에 표시
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
