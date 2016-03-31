<!--
.. title: Python'da Zincirleme Metodlar
.. slug: pythonda-zincirleme-metodlar
.. date: 2016-03-31
.. tags: python, programlama
.. category: Python, Programlama
.. description: Python'da Zincirleme Metodlar
.. type: text
-->

Zincirleme metodlar, bir sınıfa ait metodları tek seferde çağırma şeklinde çalışırlar. Burada amaç kod okunabilirliğini artırmaktır. Çalışma mantığı olarak metod kendisini döndürür ve bu sayede peşine başka bir metod eklenebilir. Çalışma şeklinden dolayı bunlara zincirleme metod yani `Chaining Methods` deniliyor. Çalışma mantığını anladık ama biraz daha açıklamak gerekiyor. Örneğin bir `Cars` sınıfında o sınıfa ait belirli metodlar bulunmakta. Bu metodların şöyle olduğunu düşünelim sahtece:

    A Sınıfı =>
        A1_Metodu =>
            ... işlemler
        A2_Metodu =>
            ... işlemler
        A3_Metodu =>
            ... işlemler

Böyle bir yapıda sınıfımızı **b** değişkenine ilklediğimizi ve metodları çağırdığımızı düşünelim. O zaman durum şu olurdu

    b = A Sınıfı
    b.A1_Metodu
    b.A2_Metodu
    b.A3_Metodu

gibi tam da burada yardımcı olarak zincirleme metod deseni geliyor önümüze. Eğer bir chaining metod olsaydı yukarıdaki gibi alt alta bir tekrar yerine şöyle olacaktı:
<!-- TEASER_END -->

    b.A1_Metodu.A2_Metodu.A3_Metodu

Evet anlatmak istediğim tam da bu oluyor. Peki bu Python'da nasıl çalışıyor? Öncelikle kısaca Cars sınıfımızı oluşturalım. Bu sınıf ise `maker, model, year, price, miles, show_detail` metodlarına sahip olsun. Eldeki veriler üzerinden sınıfımızın iskeletini oluşturalım.

```python
class Cars(object):

    def maker(self, mkr):
        # işlemler

    def model(self, mdl):
        # işlemler

    def year(self, yr):
        # işlemler

    def price(self, prc):
        # işlemler

    def miles(self, mile):
        # işlemler

    def show_detail(self):
        # detay işlemleri
```

Evet iskeletimiz böyle. Şimdi maker yani üreticinin değer döndürmesini sağlamalıyız. Yukarıda *metod kendisini döndürür ve bu sayede peşine başka bir metod eklenebilir* demiştim. O zaman bu maker metodu son olarak kendisini döndürmeli. Ve yine kendisine değer almalı. Kendi değerini ise aldığı argümana eşitlemeliyiz. Bakalım hemen:

```python
def maker(self, mkr):
    self.maker = mkr
    return self
```

`return self` ile metoda kendisini döndürme imkanı verdik. Bu işlemi **show_detail** hariç diğer metodlara da uygulayalım:

```python
class Cars:

    def maker(self, mkr):
        self.maker = mkr
        return self

    def model(self, mdl):
        self.model = mdl
        return self

    def year(self, yr):
        self.year = yr
        return self

    def price(self, prc):
        self.price = prc
        return self

    def miles(self, mile):
        self.miles = mile
        return self
```

Son olarak da bu değerleri göstereceğimiz **show_detail** metodunu yazalım. O konu aslında basit olarak bildiğimiz bir konu zaten.

```python
def show_detail(self):
    print("Maker:", self.maker, "Model:", self.model, "Year:",
          self.year, "Price:", self.price, "Miles:", self.miles)
```

Artık marka model ne var ne yok yazdıracağız hem de ekstra bir uğraş vermeden. Kullanımına bakarsak anlayacağız:

```python
c = Cars()

c.maker("Aston Martin").model("DB9").year(2004).price(149.000).miles(30).show_detail()
# Maker: Aston Martin Model: DB9 Year: 2004 Price: 149.0 Miles: 30
```

Üreticisi Aston Martin olan 2004 üretimli DB9 Model 30 Mildeki aracın fiyatının 149 bin euro olduğunu söylettik diyelim. Evet bu işlem bu kadar çıktıyı da yukarıda gördük. Kodların tamamı:

```python
class Cars:

    def maker(self, mkr):
        self.maker = mkr
        return self

    def model(self, mdl):
        self.model = mdl
        return self

    def year(self, yr):
        self.year = yr
        return self

    def price(self, prc):
        self.price = prc
        return self

    def miles(self, mile):
        self.miles = mile
        return self

    def show_detail(self):
        print("Maker:", self.maker, "Model:", self.model, "Year:",
              self.year, "Price:", self.price, "Miles:", self.miles)

c = Cars()

c.maker("Aston Martin").model("DB9").year(
    2004).price(149.000).miles(30).show_detail()
# Maker: Aston Martin Model: DB9 Year: 2004 Price: 149.0 Miles: 30
```

Kodları denediğim [ideone](https://ideone.com/1blLKY). Çalıştırılmış hali mevcut.
