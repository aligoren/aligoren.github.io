<!--
.. title: Django RSS Feed Ekleme
.. slug: django-rss-feed-ekleme
.. date: 2016-02-28
.. tags: django, python, programlama
.. category: Python, Django, Programlama
.. description: Django RSS Feed Ekleme
.. type: text
-->

Django’da RSS Feed ekleme işlemi çok basittir. Uzun uzun anlatabilir miyim diye düşündüm ancak yine de başaramam herhalde. Öncelikle yapılması gerekenleri söylemek gerekiyor sanırım.

Uygulamamız içerisine feeds.py dosyasını oluşturalım ( siz isterseniz mahmut.py deyin ) Oluşturma işlemini başarıyla yaptıysanız şimdi bu dosyanın içine sınıf oluşturmalıyız. Bunun için Django’nun [Feed Framework](https://docs.djangoproject.com/en/1.9/ref/contrib/syndication/)‘ünü çağırmak gerekiyor. Bir de slug yani url için de core kütüphanesinde bulunan reverse() işlevini çağıralım. <!--TEASER_END-->

```python
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
```

Bu işlemden sonra da RSS beslemesi olarak alacağımız modeli çağıralım. Benim çalışmamda RSS beslemesi yazdığım blogum için vardı. Blogdaki son yazıları gösterecekti. Post isimli modelimi de yine dahil ediyorum:

`from .models import Post`

Dahil etme işlemi başladıktan sonra PostFeed adında bir sınıf oluşturup, bu sınıfa daha önce import ettiğim Feed sınıfından miras almasını söylüyorum. Böylece Feed sınıfının özelliklerini kendi PostFeed sınıfımda kullanabileceğim. Kısacası şöyle bir giriş olacak:

```python
class PostsFeed(Feed):
   ...
```

Eh madem sınıfa bir giriş yaptık o zaman bu sınıfa dair bazı özellikleri, işlevleri kullanalım. Belirtmem gereken bazı şeyler var.

title değişkeni RSS feed sayfanızda başlığı gösteriyor. Hem h1 tagleri arasında hem de tarayıcı başlığında görünen kısımdır. O zaman sınıfımızı şöyle değerlendirelim:

```python
class PostsFeed(Feed):
    title = "Ali GÖREN"
```

Tüm işlemler bitince buradaki adımları kaynak kodlara bakıp görebilirsiniz. Neyse devam edelim:

link değişkeni site linkini gösteriyor. Bu link tagleri arasında görünen link. Örneğin http://localhost/link-degiskeni gibi düşünebiliriz. O zaman sınıfımızı biraz daha ilerletelim:

```python
class PostsFeed(Feed):
    title = "Ali GÖREN"
    link = "/"
```

Şimdi geldik en önemli noktaya. Açıklama kısmına. RSS belgelerine göre, RSS sayfaları için bir de açıklama kısmı olması gerekiyor. O zaman biz de bu doğrultuda description değişkenini kullanarak sınıfımızı geliştirelim:

```python
class PostsFeed(Feed):
    ...
    ...
    description = "Bu Feed ya da Site Açıklaması Olabilir"
```

Üst kısımları tekrar tekrar vermemek için üç nokta koyuyorum oralara. Şimdilik gördüğümüz üç element gerekli olan elementlerdi. İsterseniz feed_type ya da feed_copyright gibi özellikleri de kullanabilirsiniz. Her şey iyi hoş ama bu işlemler bize içerikleri getirmiyor. Evet şimdi artık Feed sınıfının işlevlerini yani fonksiyonlarını kullanabiliriz. Öncelikle tüm içerikleri çekelim. Bu içerikleri views.py dosyasındaki gibi çekiyoruz.

```python
class PostsFeed(Feed):
    ...


    def items(self):
        return Post.objects.all()
```

Buradaki **items()** işlevi Feed classını miras almamızdan dolayı geliyor. Daha sonra return ettiği bilgi ise Post modelimizde de belirttiğimiz içeriklerdir. Tıpkı bir views.py içinde oluşturulan işlevdeki çalışma gibi düşünelim. Buraya kadar güzel ancak henüz herhangi bir şekilde yine başlık, içerik vs. görüntüleyemiyoruz. Bunun için diğer işlevleri de kullanmalıyız. Öncelikle item_title() işlevini kullanarak çekilen içeriğin başlığını gösterelim.

```python
class PostsFeed(Feed):
    ...

    def item_title(self, item):
        return item.title
```

Görmüş olduğumuz gibi itemtitle işlevi de aldığı argümanın title özelliğini döndürüyor. Buradaki item.title’da title kısmı bizim modelimizde bulunan title’dır. Artık içeriklerin başlıklarını görebiliriz. Şimdi de **itemdescription()** işlevi ile içeriğin ( yazı olduğunu düşünüyoruz ) bir kısmını gösterelim:

```python
class PostsFeed(Feed):
    ...

    def item_description(self, item):
        return item.content
```

Yukarıdaki title kısmı için olan açıklamaların aynısını burası için de yapabilirim. Sadece bilmemiz gereken title ve content Post modelinden gelen değerler. Ayrıca eklemem gereken bir şey item* işlevler için return edilen değerlere HTML eklemesi yapabilirsiniz. Örneğin return item.content + "<hr />" gibi. Şimdi son olarak da içeriğin URL’sini vermeliyiz. Bunun için `itemlink()` işlevini kullanacağız:

```python
class PostsFeed(Feed):
    ...

    def item_link(self, item):
        return reverse("posts:detail", kwargs={"slug": item.slug})
```

Bu kısmı nasıl açıklayayım bilmiyorum ancak bunu yaparken Post gibi modelleriniz içerisinde getabsoluteurl() bulunması gerekebilir. kwars içerisindeki slug özelliğine denk gelen item.slug ise yine Post modelimizde belirtilen slug alanıdır. Son haliyle sınıfımıza bakalım:

```python
class PostsFeed(Feed):
    title = "Ali GÖREN"
    link = "/"
    description = "Açıklama"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse("posts:detail", kwargs={"slug": item.slug})
```

Sınıfımız hazır ancak bunu bir de URL olarak belirtmeliyiz ki feed adresine de erişebilelim. Bunun için uygulamamızın urls.py dosyasını açalım ve oluşturduğumuz feeds dosyasındaki PostsFeed ( sizinki nedir bilemem ) classını dahil edelim:

`from .feeds import PostsFeed`

Bu işlemi başarıyla yaptıysak bir URL eklemesi yapabiliriz:

```python
urlpatterns = [
    ...
    url(r'^feed/$', PostsFeed()),

]
```

Artık feed çağrısı yapıldığında PostsFeed class’ı çalışacak ve içerikleri döndürecektir. Örneğin http://localhost/feed gibi düşünelim. Hatalı olduğum nokta var ise bildirmenizden memnuniyet duyarım. Kendimce aktarmaya çalıştım.
