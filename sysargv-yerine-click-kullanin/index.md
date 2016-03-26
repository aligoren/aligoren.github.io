<!--
.. title: sys.argv Yerine Click Kullanın
.. slug: sysargv-yerine-click-kullanin
.. date: 2016-03-26 18:51:54 UTC+02:00
.. tags: python, programlama
.. category: Python, Programlama
.. description: sys.argv Yerine Click Kullanın
.. type: text
-->

Python ile konsol uygulamaları geliştirirken, konsolda bazen programı direkt olarak çağırmadan parametre kontrolü yapmamız gerekebiliyor. Örneğin şöyle bir çağrı:

`program.py --falan=filan`

Bu program basit ilkel yöntemlerce sys.argv kontrolü şeklinde yapılmakta. Ancak bunun doğruluğu için dahi uzunca uğraşmak gerekiyor.

Bu sorunu aşmak için çeşitli kütüphaneler mevcuttur. Örneğin argparse, docopt gibi kütüphaneler de bu soruna kolaylık sağlıyorlar. Ancak bunların yapıları gerçekten çok karmaşık. Örneğin argparse interspersed dediğimiz argümanların devre dışı bırakılmasını desteklemiyor. Bu güvenlik açısından bir sorun oluşturabilir. <!--TEASER_END--> Bu gibi bazı sorunlarla karşılaşmayı önlemek açısından Click, Armin Ronacher tarafından geliştirildi. Click kurulumu pip üzerinden yapılmakta.

`pip install Click`

komutu ile kurulumu yapabilirsiniz. Python 2.x ve 3.x sürümlerini desteklediğini de söylemek iyi olacaktır.

Kurulumdan sonra ilk olarak basit bir Merhaba uygulaması yapabiliriz.

```python
import click

@click.command()
def merhaba():
    click.echo('Merhaba')

if __name__ == '__main__':
    merhaba()
```

Click’i import ettikten sonra `command` decoratörünü çağırarak artık bunun click ile kontrol edileceğini söyleyebiliriz.

Ayrıca click `print()` harici kendisi `click.echo()` işlevi ile printer görevini sağlayabiliyor. İlk uygulamamız bu oldu ve çalıştırma işlemini yapalım. Sonuçlara bakalım. Örneğin bu yukarıdaki kodları hello.py adında bir dosyanın içerisine yazdığımızı varsayalım.

    ali@linux $ hello
    Merhaba

    ali@linux $ hello -h
    Error: no such option: -h

    ali@linux $ hello --h
    Error: no such option: --h  Did you mean --help?

    ali@linux $ hello --help
    Usage: hello.py [OPTIONS]

    Options:
      --help  Show this message and exit.

Merhaba kısmından daha çok otomatik oluşturulan help sayfalarının dikkatinizi çektiğini umuyorum. Evet click otomatik olarak help sayfası oluşturabiliyor. Bunu siz yapmadan yapabiliyor.

Örnek olarak ilk parametrelerimi tanımlayalım ve bununla ilgili bir program yapalım. Programın işlevi girilen adı, girilen sayı kadar yazdırmak olsun. Bunun normalde for döngüsü ile basitçe yapılacağını biliyoruz.

    sayaç => girilen sayı:
        yazdır: girilen isim


Evet sahte kodu bu şekilde. Normalde Python ile yapmak isteseydik de bu format üzerinden gidecektik. Şimdi tekrar Click ile geliştirmeye dönelim. Öncelikle `option()` ve `argument()` decoratörlerini ekleyelim ve bunlara alması gereken değerleri bildirelim. Bu eklenen değerleri de yani decoratörler içerisinde tanımlanan option ve argument değerlerini de kendimize ait olan işleve işlev değişken olarak atayalım.


```python
import click

@click.command()
@click.option('--count', default=1, help='Kac defa yazdiracagiz?')
@click.argument('isim', default='Ali')
def merhaba(count, isim):
    click.echo('Merhaba')

if __name__ == '__main__':
    merhaba()
```

Burada iki decorator ve bu decoratorlerin argümanları var. Option decoratorunun aldığı --count argümanı programa şu özelliği katar:

`program.py --count`

Daha sonra gelen ve 1 değerini almış olan `default` ise varsayılan değeri belirler. Burada varsayılan değerin belirli bir veri tipi yoktur. Ancak belirlenen veri tipini help metninde tür olarak gösterir. Biz sayaç işlemini yapacağımız için 1 dedik. Sonradan gelen `help` ise bu özelliğe dair yardım metnini gösterir. Yani program.py --help çağırıldığı zaman bu yardım metni de ayrıca gösterilir.

Argument decoratörü ise bir argüman alır. Bu argüman da ayrıca bir default değer alabilir.

    ali@linux $ hello
    Merhaba Ali

    ali@linux $ hello --help

    Usage: hello.py [OPTIONS] [ISIM]

    Options:
      --count INTEGER  Kac defa yazdiracagiz?
      --help           Show this message and exit.


Son olarak programı tamamlayalım ve belirtilen miktar adedince yazdırma işlemini yaptıralım.

```python
import click

@click.command()
@click.option('--count', default=1, help='Kac defa yazdiracagiz?')
@click.argument('isim', default='Ali')
def merhaba(count, isim):
    for i in range(count):
        click.echo('Merhaba %s' % isim)

if __name__ == '__main__':
    merhaba()
```

Kodlarımız bunlar. Konsolda şöyle çağırıyoruz.

    ali@linux $ hello --count=5 Arkadaş?
    Merhaba Arkadaş?
    Merhaba Arkadaş?
    Merhaba Arkadaş?
    Merhaba Arkadaş?
    Merhaba Arkadaş?

Evet şimdilik bu kadar.
