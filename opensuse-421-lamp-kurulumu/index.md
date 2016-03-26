<!--
.. title: OpenSUSE 42.1 LAMP Kurulumu
.. slug: opensuse-421-lamp-kurulumu
.. date: 2015-11-29
.. tags: linux, opensuse, lamp
.. category: Linux, OpenSUSE
.. description: OpenSUSE 42.1 LAMP Kurulumu
.. type: text
-->

Bilmiyorsanız söyleyeyim LAMP, Linux, Apache, MySQL ve PHP’nin kısaltılmasıdır. Bu yazıda “biz dört kişiyiz gardaş” diye bağıran bu grubun nasıl kurulacağını anlatacağım. Sırasıyla Adımlar:

    1- Apache Kurulumu

    2- MariaDB Kurulumu

    3- PHP Kurulumu

İlk sıraya Linux koymaya gerek yok biliyorsunuz :). Başlayalım o zaman.

# Apache Kurulumu

Apache, çoklu platformda çalışabilen web server’dır. İçerisinde CGI, SSL ve sanal alan adlarının da desteklendiği çoğu özellik bulunmaktadır. <!--TEASER_END--> Öncelikle Apache kurmak için Uçbirim’i açarak şu komutları girin:

`sudo zypper in apache2`

Bu komut apache2 kurulumunu yapacaktır. Daha sonra apache2’nin her başlangıçta otomatik olarak başlaması için şu iki komutu gireceğiz:

    sudo systemctl start apache2

    sudo systemctl enable apache2

Artık apache2 başlamış durumda ve aktif durumda. Varsayılan sunucu erişimi localhost tarafından sağlanmakta. Eğer uzak bir makineden erişime açık olmasını istiyorsanız güvenlik duvarınız ya da yönlendiricinize varsayılan port 80 olarak belirtebilirsiniz. Bunu OpenSUSE ile şöyle yaparız:

`sudo nano /etc/sysconfig/SuSEfirewall2`

Eğer nano yoksa komut satırına cnf nano yazarak nasıl kurulacağını görebilirsiniz.

Açılan kısımda CTRL+W yaparak arama yapacaksınız. Arama kısmında FW_CONFIGURATIONS_EXT yazarak arayın. İlk çıkan sonuç yorum satırı içerisindedir. Tekrar CTRL+W yapın ve enter’a basın. Karşınıza şöyle bir sonuç çıkacaktır:

`FW_CONFIGURATIONS_EXT = ""`

Bu kısımdaki tırnaklar arasına apache2 yazın yani:

`FW_CONFIGURATIONS_EXT = "apache2"`

olarak ayarlamanız gerekmekte. Daha sonra CTRL+X yaparak kaydedin. Karşınıza öncelikle dosya adı geliyordu sanıyorum burada direkt enter diyin. Sonraki adımda kaydetmek isteyip istemediğinizi soruyor. Türkçe ise E olarak isteyebilir. İngilizce ise Y olarak cevaplayın. Daha sonra firewall yeniden başlatılmalı:

`sudo systemctl restart SuSEfirewall2`

# Apache Test İşlemi:

Apache’yi test etmek için bir dosya oluşturalım. Bu dosyayı oluşturacağınız yol /srv/www/htdocs/ şeklinde olacaktır. Biz henüz PHP kurmadık basit olarak bir HTML dosyası oluşturalım:

`sudo nano /srv/www/htdocs/index.html`

İçerisine herhangi bir şey yazabilirsiniz ve kaydedip çıkın. Daha sonra tarayıcıdan http://localhost adresini açın. Eğer her şeyi doğru yaptıysanız oluşturduğunuz HTML dosyasının içeriğini göreceksiniz.

# MariaDB Kurulumu

MariaDB, MySQL’in forklanmış bir sürümüdür. Dinamik kolon gibi özelliklere sahiptir. O zaman kurulum için uçbirim’e şu komutu girelim:

`sudo zypper in mariadb`

Artık kurulum yapıldı. Şimdi MariaDB yani MySQL her başlangıçta başlasın istiyoruz. Aynı apache2 için yaptığımız gibi MySQL için de systemctl kullanacağız.

    sudo systemctl start mysql

    sudo systemctl enable mysql

# MySQL root Parolasını Ayarlama

MySQL root parolası varsayılan olarak boş gelir. Ancak bazı durumlarda yetkisiz erişimi engellemek isteyebilirsiniz. Bu durumda MySQL’i root parolası ile korursunuz. Bunun için konsol’a

`mysql_secure_installation`

komutunu verelim. Karşımıza dolusuna yazı gelecek. Burada size bir soru soracak.

    “Set root password? [Y/n]”

Bu kısım root parolası ayarlamak ister misiniz diyor. Y tuşuna basın. Parolanızı iki defa gireceksiniz. Her iki defasında da girmiyor gibi görünebilirsiniz. Parola gizli olarak giriliyor.

    “Remove anonymous users? [Y/n]”

Anonim kullanıcıları silmek ister misiniz diyor. Eğer silmek isterseniz Y tuşuna basın.

    “Disallow root login remotely [Y/n]”

Bu kısımda uzak root erişimini kısıtlayın diyor. Buna Y diyoruz.

    “Reload privilege tables now [Y/n]”

Tabloları baştan oluşturmak isteyip istemediğinizi soruyor. Bu kısımda da Y diyoruz. MySQL ayarlarımızı tamamladık.
PHP Kurulumu

Her şeyi kurduk. Artık PHP kurulumunu yapmamız gerekiyor. Komut satırına şu komutları girelim:

`sudo zypper in php5 php5-mysql apache2-mod_php5`

Çok fazla uzun sürmeyecek bir kurulumla bir sonraki adıma geçelim. Yani mod-php aktif olmalı. Bunun için şu komutları çalıştırıyoruz:

`sudo a2enmod php5`

# PHP’yi Test Edelim:

Basit olarak php bilgilerini veren bir PHP dosyası oluşturalım:

`sudo nano /srv/www/htdocs/info.php`

Bu dosyanın içine

```php
<?php

phpinfo();

?>
```
kodlarını ekleyelim, kaydedip çıkalım. Daha sonra apache2’yi yeniden başlatalım:

`sudo systemctl restart apache2`

Daha sonra PHP bilgilerinin olduğu dosyayı çalıştıralım:

[http://localhost/info.php](http://localhost/info.php)

adresinde düzgünce görüntüleme işlemini yaptıysanız sıkıntı yok. Eğer tüm php modüllerini kurmak istiyorsanız konsoldan şu komutu giriniz:

`sudo zypper in php*`

Daha sonra eğer geliştirme amaçlı çalışıyorsanız, çalışırken hataları görmek amacıyla bunları aktif etmelisiniz. Bu hataların yönetimini display_errors’da saklı. Varsayılan değer Off olarak geliyor. Aktif etmek için konsoldan şu komutu çalıştıralım:

`sudo nano /etc/php5/apache2/php.ini`

Daha sonra `display_errors = Off` şeklinde aratıp bu kısmı `display_errors = On` olarak değiştiriyoruz. Kaydedip çıkalım.

Tüm bunlardan sonra “permission denied” hatası almamak için chmod 777 yapmalıyız. Bu sayede “/srv/www/htdocs” ve altındaki dizinlere 777 iznini vermiş olacağız. Komut satırından şu komutu çalıştıralım:

`chmod 777 /srv/www/htdocs`

# phpMyAdmin Kurulumu

MySQL’i komut satırından kontrol etmek istemiyorsanız phpMyAdmin sizin için harika bir araç. Web arayüzü ile MySQL veritabanlarınızı yönetebilirsiniz. Kurulum için komut satırına şu komutu girelim:

`sudo zypper in phpmyadmin`

Eğer parola oluşturmanızı falan isterse MySQL için oluşturduğunuz parolayı tekrarlayın. Daha sonra “php.ini” düzenlemek için komut satırına şu komutu yazın:

`sudo nano /etc/php5/apache2/php.ini`

php.ini dosyası açıldıktan sonra şunu aratın:

`extension=php_mbstring.dll`

Burası yorum satırı olarak görünüyor. Bu kısmı yorum satırı olmaktan kurtarın. Daha sonra apache2’yi yeniden başlatın:

`sudo systemctl restart apache2`

Artık phpMyAdmin’e erişim sağlayabilirsiniz:

[http://localhost/phpMyAdmin](http://localhost/phpMyAdmin)

Evet kurulum bu kadar ve basit. İyi çalışmalar
