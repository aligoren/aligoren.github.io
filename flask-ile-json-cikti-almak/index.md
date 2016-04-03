<!--
.. title: Flask ile JSON Çıktı Almak
.. slug: flask-ile-json-cikti-almak
.. date: 2016-04-03
.. tags: python, programlama, flask
.. category: Python, Programlama, Flask
.. description: Flask ile JSON Çıktı Almak
.. type: text
-->

Flask framework'ü bilmeyen yoktur. Bu yazı hiç kullanmamış arkadaşlar için değil baştan belirteyim. Bu yazıda Flask framework ile nasıl json çıktı alırız onu anlatmaya çalışacağım.

Öncelikle flask kurulu olmalı onu biliyoruz. json çıktı alma işlemi için ben flask ile gelen jsonify metodunu tercih ediyorum. Siz isterseniz klasik json da kullanabilirsiniz. İki türlü de aynı çalışıyor. Sadece jsonify çıktıları biraz daha güzel gösteriyor. Ben bu yazı için hazırladığım uygulamada işi biraz farklı bir noktaya taşıdım ve sanki bir api varmış gibi çalışsın istedim.
<!-- TEASER_END -->

Bunun için bir API_KEY oluşturulmalı. Ben api key için uuid kullandım. Vereceğim kod parçasını sakın referans olarak almayın. Değişik bir api oluşturma kafasına sahiptim o sıra. Neyse api key oluşturma işlevi şöyle:

```python
import uuid
import random
import hashlib

def generate_key(user_name):
    uname_comp = hashlib.md5(user_name.encode()).hexdigest()
    g_key = uuid.uuid5(uuid.NAMESPACE_DNS,
                       (uname_comp + user_name + 'api_gen'))
    gt_key = str(g_key)
    gt_key = gt_key.replace("-", "")

    i_key = uuid.uuid5(uuid.NAMESPACE_DNS, (uname_comp + '127.0.0.1'))
    ip_key = str(i_key)
    ip_key = ip_key.replace("-", "")

    p_key = uuid.uuid5(uuid.NAMESPACE_X500,
                       (uname_comp + 'python' + uname_comp))
    py_key = str(p_key)
    py_key = py_key.replace("-", "")

    flsk_key = uuid.uuid5(uuid.NAMESPACE_URL, ('flask' + uname_comp))
    flk_key = str(flsk_key)
    flk_key = flk_key.replace("-", "")

    now_key = ip_key + gt_key + py_key + flk_key

    rt_key = uuid.uuid5(uuid.NAMESPACE_DNS,
                        (uname_comp + now_key + uname_comp + uname_comp))
    rtn_key = str(rt_key)
    rtn_key = rtn_key.replace("-", "")
    return rtn_key
```

Kod kötü bi pratik olduğu için değişken isimlerini vs. değiştirmedim önemli gelmedi bana sonuçta bu yazıya hazırlıyorum. Muhtemelen api key oluşturmanın daha mükemmel yolları var. Efendim gelelim Bu `generate_key` işlevi ile oluşturacağımız key'lere. Kullanımı basit tek bi argüman alıyor o da user_name. Bu argüman kullanıcı kayıt olduğu anda gelen argüman olarak oluştu diyelim. Şöyle kullanalım

```python
print(generate_key("admin"))
# "a21aacf74f79519b85581b87b8583f13"
```

Çıktı olarak buna benzer 32 karakterden oluşan bi string üretilmiş oldu. Şimdi bu api_key işlemi tamam. Bu yazı için rastgele sözler uygulaması hazırladım. Sözleri author'a göre çekecek. Herhangi bir veritabanı kullanmadım. Basit bi dictionary'den oluşuyor. O zaman author'a göre çekecekse ve api key ile olacaksa URL yapısını şöyle düşündüm:

**http://site.dev:5000/quote/author=<author>&api_key=<api_key>**

URL'den de anlaşılacağı gibi route, quote olarak ayarlanmış durumda.

```python
@app.route('/quote/author=<author>&api_key=<api_key>')
```

Artık bu route için oluşturacağımız metod iki argüman alacak. Birisi author diğeri ise api_key argümanı olacak.

```python
def quoteing(api_key, author):
    key_list = ["2bd137ea90b45b8b8902a39b6b192936",
                "3b2b6e8152475891a39297e331e8ad52",
                "26fec42ede2057ae84ed6514be7823c6",
                "a21aacf74f79519b85581b87b8583f13",
                "6968a8489e495d12976eaf25ba860423"]
```

Route için oluşturduğum işlev burada. Adına bakmayın :p. Burada key_list kısmını ben yukarıdaki generate_key işlevi ile oluşturdum. Bunlar statik keyler. Daha sonra ise işlevin aldığı argüman bu liste içinde var mı yok mu şeklinde kontrol edeceğiz:

```python
harfler = {'İ': 'i', 'Ö': 'o', 'I': 'i', 'ı': 'i',
           'Ç': 'c', 'Ğ': 'g', 'Ş': 's', 'Ü': 'u',
           'ü': 'u', 'ö': 'o', 'ş': 's', 'ç': 'c',
           'ğ': 'g'
           }


def karakter(metin, sozluk):
    for i, j in sozluk.items():
        metin = metin.replace(i, j)
    return metin

if api_key in key_list:
    quotes = {'ataturk':
              ['Hayatta En Hakiki Mursit Ilimdir Fendir',
               'Bagimsizlik, ugruna olmesini bilen toplumlarin hakkidir.'],
              'mahatma gandhi':
              ['Happiness is when what you think, what you'
               'say,and what you do are in harmony.',
               'Guc fiziki kapasiteden degil,'
               'boyun egmeyen iradeden gelir.']}

    get_quote = quotes[karakter(author.lower(), harfler)]
```

Buradaki quotes bir sözlük yani dict olduğu için key-value şeklinde çalışıyor. Biz key değerini girerek value çekebiliriz. İçeride yer alan bir karakter işlevi. Türkçe karakter sorunu yaşanıyorsa kullanılabilir. Benim url yapımda örneğin **/quote/author=Atatürk&api_key=<api_key>** şeklinde bir author çağrısında yani aslında key çağrısında karakterden dolayı sorun yaşıyordum. Onu hallettim denilebilir.

Daha sonra ise artık bu değerleri döndürmemiz gerekiyor. api key var mı yok mu kontrolü ile birlikte olacak şekilde. Burada jsonify işlevi direkt olarak dict alabiliyor. Yani herhangi bir değişkene ilklemenize gerek yok aslında. Sol değer key, sağ değer ise value gibi bir çıktı verecektir.

```python
    return jsonify(quotes=random.choice(get_quote))
else:
    return jsonify(error="API Key Not Found")
```


Son olarak da parametrelerden birisi girilmezse 404 hatası yerine yine json çıktısı üretelim:

```python
@app.errorhandler(404)
def exception_handler(e):
    return jsonify(error="404 Not Found")
```

Bu sayede 404 olacak hatalarda json haliyle çıkmış olacak. Şimdi hazırladığımız uygulamayı bi çalıştıralım ve bakalım. Öncelikle konsolda `a21aacf74f79519b85581b87b8583f13` şeklinde bir çıktı var. O generate_key işlevi ile ürettiğimiz bir çıktı bunu biliyoruz. `http://127.0.0.1:5000/` adresini açarsak eğer error anahtarlı bir uyarı göreceğiz yine çıktısı json:

```json
{
  "error": "404 Not Found"
}
```

O zaman quote url'sine yönlenelim. URL şöyle olacak `http://127.0.0.1:5000/quote/`. Bu kısma gelince ufak bi manual tarzı şey hazırlamıştım. Onu göreceğiz:

```json
{
  "USER_API_KEY": [
    "2bd137ea90b45b8b8902a39b6b192936",
    "3b2b6e8152475891a39297e331e8ad52",
    "26fec42ede2057ae84ed6514be7823c6",
    "a21aacf74f79519b85581b87b8583f13",
    "6968a8489e495d12976eaf25ba860423"
  ],
  "error": "API Key Required",
  "url_example": "/quote/author=ATATURK&api_key=API_KEY_HERE"
}
```

Biz de url_example üzerinden listedeki örnek api keyleri kullanarak gidelim. Adres yapısını şöyle seçtim `http://127.0.0.1:5000/quote/author=atatürk&api_key=a21aacf74f79519b85581b87b8583f13`. Bu haliyle şu çıktıyı veriyor:

```json
{
  "quotes": "Hayatta En Hakiki Mursit Ilimdir Fendir"
}
```

Sayfayı yeniledikçe hangi sözler var ise rastgele onu çekecek. Bizim örnekte iki tane vardı. Peki hatalı bir API girseydik? Örneğin şöyle `http://127.0.0.1:5000/quote/author=atatürk&api_key=interesting_api`. Çıktısı şöyle olacaktı:

```json
{
  "error": "API Key Not Found"
}
```

Son olarak değer girilmezse şöyle olacak. URL örneğin `http://127.0.0.1:5000/quote/author=atatürk&api_key=`

```json
{
  "error": "404 Not Found"
}
```

# Kodların Tamamı

```python
from flask import Flask, jsonify
import uuid
import random
import hashlib


app = Flask(__name__)


def generate_key(user_name):
    uname_comp = hashlib.md5(user_name.encode()).hexdigest()
    g_key = uuid.uuid5(uuid.NAMESPACE_DNS,
                       (uname_comp + user_name + 'api_gen'))
    gt_key = str(g_key)
    gt_key = gt_key.replace("-", "")

    i_key = uuid.uuid5(uuid.NAMESPACE_DNS, (uname_comp + '127.0.0.1'))
    ip_key = str(i_key)
    ip_key = ip_key.replace("-", "")

    p_key = uuid.uuid5(uuid.NAMESPACE_X500,
                       (uname_comp + 'python' + uname_comp))
    py_key = str(p_key)
    py_key = py_key.replace("-", "")

    flsk_key = uuid.uuid5(uuid.NAMESPACE_URL, ('flask' + uname_comp))
    flk_key = str(flsk_key)
    flk_key = flk_key.replace("-", "")

    now_key = ip_key + gt_key + py_key + flk_key

    rt_key = uuid.uuid5(uuid.NAMESPACE_DNS,
                        (uname_comp + now_key + uname_comp + uname_comp))
    rtn_key = str(rt_key)
    rtn_key = rtn_key.replace("-", "")
    return rtn_key

print(generate_key("admin"))

harfler = {'İ': 'i', 'Ö': 'o', 'I': 'i', 'ı': 'i',
           'Ç': 'c', 'Ğ': 'g', 'Ş': 's', 'Ü': 'u',
           'ü': 'u', 'ö': 'o', 'ş': 's', 'ç': 'c',
           'ğ': 'g'
           }


def karakter(metin, sozluk):
    for i, j in sozluk.items():
        metin = metin.replace(i, j)
    return metin


@app.route('/quote/')
def quote_index():
    url_type = '/quote/author=ATATURK&api_key=API_KEY_HERE'

    key_list = ["2bd137ea90b45b8b8902a39b6b192936",
                "3b2b6e8152475891a39297e331e8ad52",
                "26fec42ede2057ae84ed6514be7823c6",
                "a21aacf74f79519b85581b87b8583f13",
                "6968a8489e495d12976eaf25ba860423"]

    return jsonify(error="API Key Required", url_example=url_type,
                   USER_API_KEY=key_list)


@app.route("/quote/author=<author>&api_key=<api_key>")
def quoteing(api_key, author):
    key_list = ["2bd137ea90b45b8b8902a39b6b192936",
                "3b2b6e8152475891a39297e331e8ad52",
                "26fec42ede2057ae84ed6514be7823c6",
                "a21aacf74f79519b85581b87b8583f13",
                "6968a8489e495d12976eaf25ba860423"]

    if api_key in key_list:
        quotes = {'ataturk':
                  ['Hayatta En Hakiki Mursit Ilimdir Fendir',
                   'Bagimsizlik, ugruna olmesini bilen toplumlarin hakkidir.'],
                  'mahatma gandhi':
                  ['Happiness is when what you think, what you'
                   'say,and what you do are in harmony.',
                   'Guc fiziki kapasiteden degil,'
                   'boyun egmeyen iradeden gelir.']}

        get_quote = quotes[karakter(author.lower(), harfler)]

        return jsonify(quotes=random.choice(get_quote))
    else:
        return jsonify(error="API Key Not Found")


@app.errorhandler(404)
def exception_handler(e):
    return jsonify(error="404 Not Found")

if __name__ == "__main__":
    # app.debug = True
    app.run()
```

Eğer `app.debug = True` yaparsanız live olarak çalışırsınız. Yenileme yaptığınız zaman değişiklikler anında uygulanır tekrardan başlatmanıza gerek kalmaz. Evet bu kadar. Hatalı noktalarım varsa şimdiden özür dilerim.
