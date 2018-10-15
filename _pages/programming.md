---
title: Introduction to Programming
layout: default
permalink: /programming/index.html

hero: This page relates to the talk given at Cardiff University School of Mathematics on 15th October 2018. Below are the relevant files for download.
    
slideslink: 

fileslink: 

---

<p>{{ page.hero }}</p>
<br/>

<h4>Downloads:</h4>
<ul>
  <li><center><a href="https://docs.google.com/presentation/d/1MGpppVeaM3Ty6U_-uoROU2o-xN79jFMn7vivodPBkj0/export/pdf" class="btn btn-ghost" target="_blank">Slides</a> | --------- | <a href="/assets/intro.ipynb" class="btn btn-ghost" target="_blank">Files</a></center></li>
</ul>
<br/>

<h4>Resources &amp; Useful Links:</h4>
<ul>
  {% for resource in site.data.teaching_resources.common %}
    <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
  {% endfor %}
  <li><a href="/ugmatlab/" target="_blank"><em>MATLAB Final Year Course</em></a></li>
</ul>
<br/>

<br/>
