---
layout: pages
permalink: /blog/

hero: Just a few blog posts about things I've done or things I find interesting. Mainly focussed around Education, Raspberry Pi and various Outreach Projects. You can filter the posts by clicking the handy links below. Enjoy!
---

<p>{{ page.hero }}</p>
<br/>

<center>
  {% for link in site.data.blogtitles %}
    {% if link.frontshow != "none" %}
      <a href="{{ link.url }}" class="btn btn-ghost">{{ link.title }}</a>
    {% endif %}
  {% endfor %}
</center>

<br/>

<section class="post-list">

  <h2>Highlights</h2>
  {% for post in site.posts %}
    {% if post.category contains "highlight" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2>Bridgend College</h2>
  {% for post in site.posts %}
    {% if post.category contains "bridgend" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2>Outreach</h2>
  {% for post in site.posts %}
    {% if post.category contains "outreach" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2>SIAM-IMA Student Chapter</h2>
  {% for post in site.posts %}
    {% if post.category contains "SIAM" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>

  <h2>Conferences</h2>
  {% for post in site.posts %}
    {% if post.category contains "conference" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
  <br/><br/>
  
  <h2>Miscellaneous</h2>
  {% for post in site.posts %}
    {% if post.category contains "misc" %}
      {% include article.html %}
    {% endif %}
  {% endfor %}
</section>
