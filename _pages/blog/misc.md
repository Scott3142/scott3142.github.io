---
layout: pages
permalink: /blog/misc/
---

<center>
  {% for link in site.data.blogtitles %}
    <a href="{{ link.url }}" class="btn btn-ghost">{{ link.title }}</a>
  {% endfor %}
</center>

<br/>

<section class="post-list">

  <h2>Miscellaneous</h2>
  {% for post in site.posts %}
    {% if post.category contains "misc" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  
</section>
