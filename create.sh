DATE=`date +%Y-%m-%d`
TITLE="Başlık"
SLUG=$1

echo "---
layout: post
title: $TITLE
---" >> _posts/$DATE-$SLUG.md
