---
layout: pages
permalink: /blog/

hero: Just a few blog posts about things I've done or things I find interesting. Mainly focussed around Education, Raspberry Pi and various Outreach Projects. You can filter through the posts by clicking the handy links below. Enjoy!
---

<p>{{ page.hero }}</p>
<br/>

<center>
  <a href="/blog/bridgend/" class="btn btn-ghost">Bridgend College</a>
  <a href="/blog/education" class="btn btn-ghost">Education</a>
  <a href="/blog/siam" class="btn btn-ghost">SIAM-IMA</a>
  <a href="/blog/misc" class="btn btn-ghost">Miscellaneous</a>
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
