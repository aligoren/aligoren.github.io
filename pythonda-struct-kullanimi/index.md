<!--
.. title: Python'da Struct Kullanımı
.. slug: pythonda-struct-kullanimi
.. date: 2016-03-30
.. tags: python, programlama
.. category: Python, Programlama
.. description: Python'da Struct Kullanımı
.. type: text
-->

Evet var olmaz demeyin lütfen. Kısacası struct bir şablon olarak gelir önümüze. Bildiğimiz manada struct, farklı verileri bir araya getiriyoruz yani aslında grupluyor. Peki kullanımı nasıldı ki **"Python'da"** ile başlayan bir başlık attım ki?

Örneğin D dilinden örnek verecek olursak Ali Çehreli hocam çok güzel [açıklamış](http://ddili.org/ders/d/yapilar.html):
<!-- TEASER_END -->

```d
struct GununSaati {
    int saat;
    int dakika;
}
```

Bu D dili ile yazılan bir örnek. Ve oradan bir alıntı yapmak istiyorum:

    struct birbirleriyle ilişkili değişkenleri bir araya getirerek yeni bir tür olarak kullanma olanağı verir:

Benim de yukarıda söylediğimle aynı aslında. Ve sonrasında alt kısımda bir açıklama daha getirilmiş.

    Yukarıdaki tanım, saat ve dakika isimli iki int değişkeni bir araya getiren ve ismi GününSaati olan yeni bir tür tanımlar.
    Yukarıdaki tanımdan sonra artık başka türler gibi kullanabileceğimiz GününSaati isminde yeni bir türümüz olur.
    Örnek olarak int türüne benzer kullanımını şöyle gösterebiliriz:

Evet buraya kadar biraz anlam çıkarılmış olmalı sanıyorum ki. Peki bunu Python'da nasıl yaparız?

![/galleries/inte/cat.png](/galleries/inte/cat.png)

Bunun için öncelikle collections kullanmamız gerekiyor. Ve buradan dahil edeceğimiz namedtuple da struct'ımızı oluşturmamızda bize yardımcı olacak. Basit bir anlatım yapmaya çalışayım. Bir `namedtuple` için.

namedtuple ilk argüman olarak Tip Adı olarak kabul edilen bir argüman [alır](https://docs.python.org/dev/library/collections.html#collections.namedtuple). Diğer işe yarar argüman ise bu bize özgü tipe ait alanlardır. Yukarıdaki D dili örneğine tekrar bakarsak saat ve bakika, yazacağımız python kodunda bizim alanlarımız olacaktır. Temelde kod yapısı şöyle olacaktır:

```python
namedtuple("TipAdı", "tip_alanı ikinci_alan üçüncü_alan")
```
O zaman bir örnek kod görelim bu anlamamız açısından daha iyi olacaktır.

```python
from collections import namedtuple

YeniTip = namedtuple('GununSaati', "saat dakika")
```

Öncelikle namedtuple'ı çağırdık bunu söylemiştim. namedtuple'ı bir değişkene atadım aslında artık namedtuple'ın işlerini `YeniTip` yönetecek. Burada namedtuple `GununSaati` adında yeni bir tür oluşturdu. Bu türün alanları ise saat ve dakika oluyor. Tür dediğim kısım aslında tip kısmı. Zaten verdiğim açıklama linkine de bakarsanız oranın alacağı parameter **TypeName** olarak belirtilmiş. Peki yeni türümüzü hazırladık nasıl kullanacağız?

Öncelikle bu yeni tipimizi bir değişkene ilkleyelim. Bu ilkleme sırasında YeniTip argüman alan bir işlev gibi davranacak. Bunu bir kod ile görelim:

```python
zaman = YeniTip(15, 30)
```

Oluşturduğumuz zaman değişkeni, YeniTip olarak ilklediğimiz veri tipine ilklendi. Artık **zaman** değişkeni ile istediğim alanlara erişebilirim. Bu örnekte alanlarımız saat ve dakika idi. Örnekte 15 saat, 30 ise dakika oluyor. Şu an yazdığımız kodların tam haline bakalım:

```python
from collections import namedtuple

YeniTip = namedtuple('GununSaati', "saat dakika")

zaman = YeniTip(15, 30)

print(zaman.saat)
print(zaman.dakika)
```

Bu kodun verdiği çıktı 15 ve 30 olacaktır. Eğer özel bir tür var ise yani **GununSaati** gibi bir tür var ise bu türe ait alanları öğrenmek yine çok basit. Yukarıdaki zaman değişkeni üzerinden gidecek olursak şöyle açıklayayım:

```python
print(zaman._fields) # print(zaman._fields)
```

ya da henüz herhangi bir değer almamış hali ile yani saf hali ile tip üzerinden kontrolü şöyle sağlarız:

```python
print(YeniTip._fields)
```

Bu sayede değer girmek zorunda kalmamış oluruz. Ayrıca dikkat etmemiz gereken bir diğer husus ise değeri bir kere verilmiş namedtuple'a daha sonra tekrar değer veremiyorsunuz. Yani şunu yapamazsınız

```python
zaman = YeniTip(15, 30)
zaman.saat = 20
```

Eğer bunu yaparsanız şöyle bir hata alırsınız:

    Traceback (most recent call last):
      File "test.py", line 6, in <module>
        zaman.saat = 20
    AttributeError: can't set attribute

Hmm diyor ki bir değer set edemezsiniz. O yüzden eğer yapılara bir değer vereceksek ilklediğimiz anda bu değerleri vermemiz gerekiyor. Ancak bu dinamik değerler alamaz demek değildir. Örnek verecek olursak:

```python
from collections import namedtuple

saat = [10, 11, 12, 13, 14, 15]

YeniTip = namedtuple('GununSaati', "saat dakika")

for sa in saat:
    zaman = YeniTip(sa, 30)
    print(zaman.saat, ":", zaman.dakika)

"""
10 : 30
11 : 30
12 : 30
13 : 30
14 : 30
15 : 30
"""
```

Yukarıdaki örneği verdim. Aslında bunu iterable hale getirmemizi sağlayan `_make` işlevi var. Örneğin;

```python
from collections import namedtuple
saat_dakika = [15, 30]
YeniTip = namedtuple("GununSaati", "saat dakika")
YeniTip._make(saat_dakika)
# GununSaati(saat=15, dakika=30)
```

Makaleyi yanlışa götürmemek adına yukarıdaki set edilemez hatasına farklı bir açıdan yaklaşalım. Evet direkt olarak bir set etme işlemi yapamıyoruz ancak `_replace` işlevi ile değeri değiştirebiliriz. Fakat bunu tanımlamadan hemen sonra yapmalıyız. Örnek şöyle olmalı:

```python
from collections import namedtuple

YeniTip = namedtuple('GununSaati', "saat dakika")

zaman = YeniTip(15, 30)

zaman = zaman._replace(saat=19)

print(zaman.saat) # 19
```

Son olarak da zaman değişkenine type kontrolü yapalım.

```python
from collections import namedtuple

YeniTip = namedtuple('GununSaati', "saat dakika")

zaman = YeniTip(15, 30)

zaman = zaman._replace(saat=19)

print(type(zaman))

# <class '__main__.GununSaati'>
```

Artık bu nesnenin türünün GununSaati olduğunu görebiliyoruz. Hatalı bir nokta var ise şimdiden özür dilerim.
