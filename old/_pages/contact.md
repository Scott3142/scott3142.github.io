---
title: Contact
layout: default
permalink: /contact_old/
---

{% for contactlink in site.data.social %}
  <p>{{ contactlink.title }} : <a href="{{ contactlink.url }}" target="_blank">{{ contactlink.linkname }}</a></p>
{% endfor %}
