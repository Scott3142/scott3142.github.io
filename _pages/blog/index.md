---
layout: pages
permalink: /blog/
---

<section class="post-list">
  {% for post in site.posts %}
    {% include article.html %}
  {% endfor %}

  {% include pagination.html %}
</section>