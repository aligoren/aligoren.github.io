<!--
.. title: Hamming Sayıları
.. slug: hamming-sayilari
.. date: 2015-11-15
.. tags: python, programlama
.. category: Python, Programlama
.. description: Hamming Sayıları
.. type: text
-->

Hamming sayıları, 2,3 ve 5’ten başka diğer asal bölene sahip olmayan dizilerdir. Örnek verecek olursak hamming dizisi şöyledir.

İlk 60 Hamming Sayısı: 2 3 4 5 6 8 9 10 12 15 16 18 20 24 25 27 30 32 36 40 45 48 50 54 60… şeklinde gider.

Sıradaki sayının bulunması üç farklı durumdan oluşmakta. Sayı 2’ye bölünebiliyorsa bir sonraki aşamada 2,3 ve 5 dışında böleni olmayacak.

Örneğin şöyle izah edilebilir. <!--TEASER_END-->

hamming_numbers.py

```python
if x % 2 == 0:
        return is_hamming_numbers(x/2)
```

Bu sayede artık var olan sayı elimizdeki dizideki sayılardan birisi durumunda. Örneğin 60/2 sonuç olarak 30 veriyor. Diziye baktığımızda 30’dan büyük ilk sayımız 32. Buna göre 2x32=64 olmakta. Yani 60’tan sonra sayı 2’ye bölünebiliyorsa bu da 2x32=64 olacaktır. Bu durum 3 ve 5 için de yine aynı şekilde anlaşılmaktadır.

Ben 9830’a kadar olan sayıları bulmak istedim. Tabii 9830 kafama göre değildi. İlk stackoverflow hatasını alacağım noktayı aramam uzun sürmedi.

O durumda aldığım hata `Python: Maximum recursion depth exceeded` hatası di. Yani yineleme derinliğinin aşıldığına dair bir hata mesajı.

Bunun için sys modülünü kullanarak izin verilen recursion aralığını değiştirebiliriz.

```python
import sys
sys.getrecursionlimit() # ayarlanmadan önceki gerçek limit
sys.setrecursionlimit(10000) # limiti 10.000'e ayarla
sys.getrecursionlimit() # limiti göster
```

setrecursionlimit yineleme limitini belirlemekte kullanılır. Biz bu denememizde özyinelemeli işlev kullandık. Bu özelliği threading modülünün stack_size işlevini kullanarak yükseltebilirsiniz. Var olan limiti yukarıdaki kodda görebiliriniz. getrecursionlimit özelliği size bu değeri verecektir.

hamming_numbers.py

```python
import sys
sys.setrecursionlimit(10000)

def is_hamming_numbers(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return is_hamming_numbers(x/2)
    if x % 3 == 0:
        return is_hamming_numbers(x/3)
    if x % 5 == 0:
        return is_hamming_numbers(x/5)
    return 0

def hamming_numbers(x):
    if x == 1:
        return 1
    hamming_numbers(x-1)
    if is_hamming_numbers(x) == True:
        print("%s" % x, end=' ')

def hamming_numbers_main():
    sys.stdout.write("Hamming Numbers: ")
    hamming_numbers(9830)

hamming_numbers_main()
```

Bu da 9830. sayıya kadar olanları yazdırmayı denediğim profile sonucu:

    python -m profile hamming_numbers.py

             37722 function calls (10704 primitive calls) in 0.156 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          347    0.000    0.000    0.000    0.000 :0(charmap_encode)
            1    0.000    0.000    0.140    0.140 :0(exec)
          173    0.000    0.000    0.000    0.000 :0(print)
            1    0.016    0.016    0.016    0.016 :0(setprofile)
            1    0.000    0.000    0.000    0.000 :0(setrecursionlimit)
            1    0.000    0.000    0.000    0.000 :0(write)
          347    0.000    0.000    0.000    0.000 cp857.py:18(encode)
            1    0.000    0.000    0.140    0.140 hamming_numbers.py:1(<module>)
       9830/1    0.062    0.000    0.140    0.140 hamming_numbers.py:15(hamming_numb
    ers)
            1    0.000    0.000    0.140    0.140 hamming_numbers.py:22(hamming_numb
    ers_main)
    27018/9829    0.078    0.000    0.078    0.000 hamming_numbers.py:4(is_hamming_n
    umbers)
            1    0.000    0.000    0.156    0.156 profile:0(<code object <module> at
     0x0178C390, file "hamming_numbers.py", line 1>)
            0    0.000             0.000          profile:0(profiler)

# Kaynaklar:

[http://stackoverflow.com/questions/8177073/python-maximum-recursion-depth-exceeded](http://stackoverflow.com/questions/8177073/python-maximum-recursion-depth-exceeded)

[http://stackoverflow.com/questions/25064781/python-hamming-number-explanation](http://stackoverflow.com/questions/25064781/python-hamming-number-explanation)

[http://codegolf.stackexchange.com/questions/7/hamming-numbers](http://codegolf.stackexchange.com/questions/7/hamming-numbers)

[http://en.wikipedia.org/wiki/Regular_number](http://en.wikipedia.org/wiki/Regular_number)
