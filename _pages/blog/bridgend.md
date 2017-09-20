---
layout: pages
permalink: /blog/bridgend

---

<center>
  <a href="/blog/" class="btn btn-ghost">All</a>
  <a href="/blog/bridgend/" class="btn btn-ghost">Bridgend College</a>
  <a href="/blog/education" class="btn btn-ghost">Education</a>
  <a href="/blog/siam" class="btn btn-ghost">SIAM-IMA</a>
  <a href="/blog/misc" class="btn btn-ghost">Miscellaneous</a>
</center>

<br/>

<section class="post-list">

  <h2 id="bridgend">Bridgend College</h2>
  {% for post in site.posts %}
    {% if post.category == "bridgend" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  
</section>
