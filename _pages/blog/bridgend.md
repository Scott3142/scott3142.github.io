---
layout: pages
permalink: /blog/bridgend/
---

<center>
  {% for link in site.data.blogtitles %}
    <a href="{{ link.url }}" class="btn btn-ghost">{{ link.title }}</a>
  {% endfor %}
</center>

<br/>

<section class="post-list">

  <h2>Bridgend College</h2>
  {% for post in site.posts %}
    {% if post.category contains "bridgend" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  
</section>
