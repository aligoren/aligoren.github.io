<!--
.. title: OpenSUSE Güncellemesini Zypper İle Yapma
.. slug: opensuse-guncellemesini-zypper-ile-yapma
.. date: 2015-11-28
.. tags: linux, opensuse
.. category: Linux, OpenSUSE
.. description: OpenSUSE Güncellemesini Zypper İle Yapma
.. type: text
-->

Öncelikle güncelleme depolarını tanımlayalım ve aktif edelim:

`sudo zypper repos --uri`

Daha sonra zypper ile depoları yenileyelim. Ve sonrasında update edelim:

    sudo zypper refresh

    sudo zypper update

Güncelleme işlemi artık başlamıştır.

Repoların tanımlı olduğu yol ise burada:

`/etc/zypp/repos.d`

Kolay gelsin.
