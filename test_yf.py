import yfinance as yf

print("yfinance test başlıyor...")
t = yf.Ticker("THYAO.IS")
df = t.history(period="1mo", interval="1d")
print(f"THYAO.IS → Bar sayısı: {len(df)}")
print(f"Sütunlar: {list(df.columns)}")
if len(df) > 0:
    print(df.tail(3))
else:
    print("⚠️ BOŞ VERİ GELDİ — Yahoo Finance bu IP'yi engelliyor!")

# İkinci test
t2 = yf.Ticker("AAPL")
df2 = t2.history(period="1mo", interval="1d")
print(f"\nAAPL → Bar sayısı: {len(df2)}")
