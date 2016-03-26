<!--
.. title: Hanoi Kuleleri Algoritması
.. slug: hanoi-kuleleri-algoritmasi
.. date: 2015-11-16
.. tags: python, programlama
.. category: Python, Programlama
.. description: Hanoi Kuleleri Algoritması
.. type: text
-->

Hanoi kuleleri, Fransız matematikçi, Edouard Lucas tarafından önerilen bir çözüm yöntemidir. A,B ve C gibi dik konumda yerleştirilmiş üç çubuk ve N kadar disk içermektedir. İşleyiş şöyledir:

Başlangıçta diskler, üstteki her diskin çapı daha büyük olmak şartıyla A çubuğuna yerleştirilir. Her seferinde sadece bir diskin hareketine izin verildiğinde, büyük disk, küçük diskin üzerine yerleştirilmeden, disklerin C çubuğuna taşınması gerekmektedir.

Hanoi problemi, problem alt problemlere parçalanarak çözülebilir. Problemde N kadar disk olduğunu varsayarsak recursive şekilde bir çözüm şu şekilde olabilir:

Sadece bir disk direkt olarak 3. çubuğa konulur N kadar disk 3. adıma yerleştirilmeli <!--TEASER_END--> Bu da şöyle uygulanabilir.

- (N-1) olan disk orta çubuğa taşınır.

- En altta kalan disk direkt sağa konulur.

- (N-1) olan disk sağa taşınır.

Örneğin 4 diskli bir çözüm uyguladığımızı varsayalım. Bunun çıktısı şöyle olur:

    Diski A çubuğundan B çubuğuna koy
    Diski A çubuğundan C çubuğuna koy
    Diski B çubuğundan C çubuğuna koy
    Diski A çubuğundan B çubuğuna koy
    Diski C çubuğundan A çubuğuna koy
    Diski C çubuğundan B çubuğuna koy
    Diski A çubuğundan B çubuğuna koy
    Diski A çubuğundan C çubuğuna koy
    Diski B çubuğundan C çubuğuna koy
    Diski B çubuğundan A çubuğuna koy
    Diski C çubuğundan A çubuğuna koy
    Diski B çubuğundan C çubuğuna koy
    Diski A çubuğundan B çubuğuna koy
    Diski A çubuğundan C çubuğuna koy
    Diski B çubuğundan C çubuğuna koy

- 4 adet disk kullanılan bir durumda n = 1 oluyorsa toplam 3 durum ve çözüm için K1 = 1 olur.

- Yine disk sayısının n = 2 olduğu durumda toplam 9 durum ve çözüm için K2 = 3 olur.

- n = 3 disk sayısında 27 durum ve çözüm için K3 = 7 olmakta.

- Disk sayısı n = 4 olduğunda toplam durum sayısı 81 ve çözüm ise K4 = 15 olur.

Çubuk sayısı 3 olduğunda N adet disk için en düşük geçişler, recursive biçinmde Kn = (2 Kn-1 +1) ya da n’ye bağlı şekilde Kn = 2^n – 1 şeklinde bulunmaktadır.

Bu durumun Python ile çözümlenmiş hali ise şöyledir. Algoritmanın ana işlenilen işlevi hanoitoweralgorithm ile tanımlanıp 4 parametre alır. Bu işlev, parametreleri recursive olarak işler.

```python
def hanoi_tower_algorithm(n, x, y, z):

    if n == 1:
        print("Diski %s çubuğundan %s çubuğuna koy" % (x,z))
    else:
        hanoi_tower_algorithm(n-1, x, z, y)
        hanoi_tower_algorithm(1, x, y, z)
        hanoi_tower_algorithm(n-1, y, x, z)
```

Disk sayısının belirlenmesi içinse ayrıca bir işlev oluşturulur. Tek parametre alır. Bu parametre çözümdeki N disk sayısını belirtir. N adet disk bu işlevde belirtilir. Buradan alınan parametre bir üstteki ana işlevine yollanılır. Ve diskler de A, B ve C şeklinde parametre olarak yollanılır.

```python
def hanoi_tower_algorithm_main(ndisc):
    # ndisc = Number of Disc
    hanoi_tower_algorithm(ndisc, "A", "B", "C")
```

10 adet disk için çıkarılan profile sonucu ise şöyledir:

    python -m profile hanoi_tower_algorithm.py

             6654 function calls (5121 primitive calls) in 0.078 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         2046    0.000    0.000    0.000    0.000 :0(charmap_encode)
            1    0.000    0.000    0.078    0.078 :0(exec)
         1023    0.062    0.000    0.078    0.000 :0(print)
            1    0.000    0.000    0.000    0.000 :0(setprofile)
         2046    0.016    0.000    0.016    0.000 cp857.py:18(encode)
            1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(<module
    >)
       1534/1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(hanoi_t
    ower_algorithm)
            1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:44(hanoi_
    tower_algorithm_main)
            1    0.000    0.000    0.078    0.078 profile:0(<code object <module> at
     0x01DCC2A0, file "hanoi_tower_algorithm.py", line 1>)
            0    0.000             0.000          profile:0(profiler)

# Kaynaklar:

[Sadri Evren Şeker](http://bilgisayarkavramlari.sadievrenseker.com/2012/03/15/hanoi-kuleleri-towers-of-hanoi/)
