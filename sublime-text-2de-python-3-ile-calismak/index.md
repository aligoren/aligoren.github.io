<!--
.. title: Sublime Text 2’de Python 3 ile Çalışmak
.. slug: sublime-text-2de-python-3-ile-calismak
.. date: 2013-08-24
.. tags: python, programlama
.. category: Python, Programlama
.. description: Sublime Text 2’de Python 3 ile Çalışmak
.. type: text
-->

Selam. Sublime Text 2 kullanan arkadaşlar default olarak “python” tanımlı olarak geliyor. Ancak Python3 gerektiren yerlerde maalesef kullanamıyoruz.

Bunu şöyle çözmek mümkün öncelikle konsola şu görseldeki komutu veriyoruz
<!-- TEASER_END -->

![](https://3.bp.blogspot.com/-HXL4T5rEYMk/Ug0DMOsr3BI/AAAAAAAAA0I/5nkLDfmJEsI/s1600/st21.png)

Şimdi bu dizine gelip istersek ls -li ile dosyaları dizinleri listeletmeye çalışabiliriz fakat şu komutu seçelim.

Daha sonra şu komutu ekrana girelim:

`gedit Python.sublime-build`

![](https://2.bp.blogspot.com/-0b_ZkLQpz9c/Ug0DsJGOkHI/AAAAAAAAA0Q/jp67tE_ozLU/s1600/st22.png)

Daha sonra açılan metin belgesindeki şu görünen kısmı

![](https://1.bp.blogspot.com/-pz358n8UFYA/Ug0EGcSiyhI/AAAAAAAAA0c/NFdkmIJNOr0/s1600/st23.png)

Yani

Kod olarak:

```json
{
 "cmd": ["python", "-u", "$file"],
 "file_regex": "^[ ]*File "(...*?)", line ([0-9]*)",
 "selector": "source.python"
}
```

Olan kısmı şununla değiştirelim:

```json
{
 "cmd": ["python3", "-u", "$file"],
 "file_regex": "^[ ]*File "(...*?)", line ([0-9]*)",
 "selector": "source.python"
}
```

Ve farklı kaydet ile Python3.sublime-build olarak kaydedelim. Zaten farklı kaydet işlemini açınca çalıştığımız dizine kaydedecektir gedit onu.

Artık sublime text 2 ile python3 kullanabiliyoruz. Bir örnek şu anki çalışmadan

![](https://1.bp.blogspot.com/-8hOI2NkG26g/Ug0FYDW2IhI/AAAAAAAAA0s/m7VoLfZLjic/s1600/st4.png)
