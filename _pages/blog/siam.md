---
layout: pages
permalink: /blog/siam/
---

<center>
  {% for link in site.data.blogtitles %}
    <a href="{{ link.url }}" class="btn btn-ghost">{{ link.title }}</a>
  {% endfor %}
</center>

<br/>

<section class="post-list">

  <h2>SIAM-IMA Student Chapter</h2>
  {% for post in site.posts %}
    {% if post.category contains "SIAM" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  
</section>
