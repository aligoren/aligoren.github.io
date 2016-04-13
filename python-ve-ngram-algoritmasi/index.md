<!--
.. title: Python ve NGram Algoritması
.. slug: python-ve-ngram-algoritmasi
.. date: 2016-04-13 22:33:15 UTC+03:00
.. tags: python, programlama
.. category: Python, Programlama
.. description: Python ve NGram Algoritması
.. type: text
-->

Bu yazıyı yazmadan önce google'da sayısızca arama yapıyordum. Beni çıldırtan bir olay oldu. Şimdi aradığım şey örneğin **ahmet** tamam iyi hoş arıyorsun da. Gelip bana neden "Bunu mu denemek istediniz?" şeklinde soru soruyorsun. Neyse önerdiği şeye tıklıyorum. Hobaa. Eski yazdığımı öneriyor bu sefer.

Meselenin aslı şu. Ne yazmaya çalıştığımı nasıl olur da bilebilir ki google? Pek de bildiği söylenemez :P. Bu yazıda anlatmaya çalışacağım NGram tarzı bir algoritma kullandıkları kesin. Bakarsınız onlar tam da bunu kullanıyorlardır.
<!--TEASER_END-->

Bu işlem temelde "ali yanlış söyler, ahmet düzeltir" mantığına dayalı. Bunu gündelik hayatta yapmak, programlamada yapmaya göre daha basit. O yüzden bizim için bunu basitleştirecek olan [ngram](https://pypi.python.org/pypi/ngram) kütüphanesini kullanabiliriz.

#NGram Kütüphanesi Kurulumu

Kurulum basit şekilde

`pip install ngram`

komutu ile yapılıyor. İlk basit örneğimize geçelim:

Öncelikle ngram'ı import edelim:

```python
from ngram import NGram
```

Bu işlemi yaptıktan sonra ngram içerisine bir dizi değeri atamamız lazım. Örneğin programlama dillerinin kontrolünün yapılmasını istiyoruz:

```python
prog_dilleri = ["php", "python", "csharp", "cpp",
                "ruby", "java", "haskell", "erlang"]
```

Bu dillerin girili olması lazım. Burada yaptığımız şey **harf bigramı** oluyor. Pekala öyleyse o zaman bu dilleri NGram ağacına ekleyelim. Yani aslında NGram nesnesine gönderiyoruz:

```python
v = NGram(prog_dilleri)
```

Çok basit şekilde ilerliyoruz. Dizi değerlerimiz artık NGram ağacına takılı durumda. Artık burada kendimize göre işlemler yapabiliriz. Bu işlemlerden birisi ise tahmin ettiğimiz gibi diller arasında arama yapmak ve en yakın olanını bulmak. O zaman bunu yapan bi metod oluşturalım.

```python
def arama(ara):
    for i in v.search(ara, threshold=0.1):
        print("Sonuç:", i[0])
```

Evet burada bakmamız gereken kısım `v.search()` kısmı. search işlevi ilk argümanda kullanıcının atadığı değeri alır. Bu değer, daha önceden girili olan değerlere benzer mi değil mi kontrolü yapılır. Yani Örneğin **prog_dilleri** dizisindeki python ile payton ne kadar benzer şeklinde sorar. Gelelim `threshold` değerine. Bu değer girilen değerin, veritabanında yani NGram ağacındaki benzerine olan yakınlık durumunu sorgular. Bu yakınlık eşiğini kontrol için vardır. Genel itibariyle programımızın kodları şöyle:

```python
from ngram import NGram

prog_dilleri = ["php", "python", "csharp", "cpp",
                "ruby", "java", "haskell", "erlang"]

v = NGram(prog_dilleri)

def aramaYap(ara):
    for i in v.search(ara, threshold=0.1):
        print("Önerilen:", i[0], "-- Yakınlık:", i[1], "\n")

aramaYap("payton")
```

Programımızı çalıştırınca şöyle oluyor:

    Önerilen: python -- Yakınlık: 0.23076923076923078

Evet bu kadardı arkadaşlar. İsterseniz NGram dokümanlarına [buradan](https://pythonhosted.org/ngram/ngram.html) ulaşabilirsiniz.
