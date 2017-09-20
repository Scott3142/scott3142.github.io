---
layout: pages
permalink: /blog/conferences/
---

<center>
  {% for link in site.data.blogtitles %}
    <a href="{{ link.url }}" class="btn btn-ghost">{{ link.title }}</a>
  {% endfor %}
</center>

<br/>

<section class="post-list">

  <h2>Conferences</h2>
  {% for post in site.posts %}
    {% if post.category contains "conference" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  
</section>
