---
layout: pages
permalink: /blog/
---

<center>
  <a href="/blog/index.html#bridgend" class="btn btn-ghost">Bridgend College</a>
  <a href="/blog/index.html#education" class="btn btn-ghost">Education</a>
  <a href="/blog/index.html#siam" class="btn btn-ghost">SIAM-IMA</a>
  <!--<a href="/blog/index.html#misc" class="btn btn-ghost">Miscellaneous</a>-->
</center>

<br/>

<section class="post-list">

  <h2>Highlights</h2>
  {% for post in site.posts %}
    {% if post.category == "highlight" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2 id="bridgend">Bridgend College</h2>
  {% for post in site.posts %}
    {% if post.category == "bridgend" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2 id="education">Education</h2>
  {% for post in site.posts %}
    {% if post.category == "education" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2 id="siam">SIAM-IMA Student Chapter</h2>
  {% for post in site.posts %}
    {% if post.category == "SIAM" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <!--<h2 id="misc">Miscellaneous</h2>-->
  {% for post in site.posts %}
    {% if post.category == "misc" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
</section>
