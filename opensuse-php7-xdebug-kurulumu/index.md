<!--
.. title: OpenSuSe PHP7 XDebug Kurulumu
.. slug: opensuse-php7-xdebug-kurulumu
.. date: 2016-02-18
.. tags: linux, opensuse, xdebug, php
.. category: Linux, OpenSUSE
.. description: OpenSuSe PHP7 XDebug Kurulumu
.. type: text
-->

PHP7 çıkalı baya oluyor. XDebug geliştiriciler için hata ayıklama aracı. Gerçekten çok faydalı bir araç. Bu aracı PHP7 için OpenSuSe’a kurmaya çalışırsanız depolarında bulamıyorsunuz. Depolarda php5-xdebug bulunmakta. Fazla uzatmadan konuya gireyim can sıkıcı bir makale olmasın.

XDebug kurmak için öncelikle PHP7 Devel gerekiyor. PHP7 Devel kurulumunu uçbirimden zypper yardımı ile kuralım. <!--TEASER_END-->

`sudo zypper install php7-devel`

Daha sonra ise xdebug sitesinden son sürümü indirelim (Bu yazıyı yazarken en son 2.4.0 RC4 Sürümü Vardı):

`wget http://xdebug.org/files/xdebug-2.4.0rc4.tgz`

Evet wget yardımı ile indirme işlemini yaptıktan sonra arşivi açalım:

`tar -xzf xdebug-2.4.0rc4.tgz`

Arşivi açtıktan sonra klasörün içerisine gidelim:

`cd xdebug-2.4.0RC4/`

Klasöre girdikten sonra aşağıdaki komutları sırasıyla veriyoruz:

    phpize
    ./configure --enable-xdebug
    make
    sudo cp modules/xdebug.so /usr/lib/.

Burada phpize derleme aracıdır. Geri kalanı ise derleme işlemi. En son olarak da cp ile oluşturulan kütüphane dosyasını lib klasörüne taşıyoruz. Tüm bu işlemler bittikten sonra php7 içerisindeki conf.d klasörüne gidiyoruz. Ve orada 20-xdebug.ini adında bir dosya oluşturuyoruz.

    cd /etc/php7/conf.d
    sudo nano 20-xdebug.ini

Evet xdebug ini dosyasını oluşturduk. Şimdi sıra içerisine ekleyeceğimiz ayar stringlerinde. Yukarıda nano ile dosyayı açtığımızı varsayıyorum kapatmayın yani henüz oluşmadı aslında ama kaydedince oluşacak :) Sonra şu aşağıdaki stringleri ekliyoruz.

    zend_extension=/usr/lib/xdebug.so
    xdebug.remote_enable=1

Sonunda işlemler tamamlandı artık apache ya da nginx ne kullanıyorsanız onu yeniden başlatabilirsiniz. Nginx kullananlar aynı işlemi fpm klasöründeki conf.d için de yapabilirler. Yükleme işleminin kontrol için konsoldan php -v komutunu verin.

    PHP 7.0.3 (cli) ( NTS )
    Copyright (c) 1997-2016 The PHP Group
    Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
       with Xdebug v2.4.0RC4, Copyright (c) 2002-2016, by Derick Rethans

Eğer çıktı yukarıdaki gibi ise yani with Xdebug yazısını görüyorsanız kurulum başarılı olmuştur. Bu kadar
