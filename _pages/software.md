---
title: BTEC First Diploma - Level 2
coursename: Automated Computer Systems
layout: default
year: 2017/2018
permalink: /software/

hero: |
  This page relates to the <em>BTEC First Diploma</em> course <em>Automated Computer Systems</em> running at Bridgend College during the academic year 2017/2018. Course notes and program files will be available to download here and will be updated as new material is added. Comments and questions welcome at any time.

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Scott Morgan</a> (<a href="mailto:smorgan@bridgend.ac.uk" target="_blank">smorgan@bridgend.ac.uk</a>). Support will be provided via e-mail or during class.
---

<p>{{ page.hero }}</p>
<br/>

<h4>Resources:</h4>
<ul>
  {% for resource in site.data.software.resources %}
    <li><center><a href="{{ resource.url }}" class="btn btn-ghost" target="_blank"><em>{{ resource.text }}</em></a></center></li><br/>
  {% endfor %}
</ul> 
<br/>

<h4>Slides:</h4>
<ul>
  {% for slide in site.data.software.slides %}
    <li><center><a href="{{ slide.url }}" class="btn btn-ghost" target="_blank"><em>{{ slide.text }}</em></a></center></li><br/>
  {% endfor %}
</ul> 
<br/>

<h4>Course Files:</h4>
<ul>
  {% for link in site.data.software.links %}
    <li><center><a href="{{ link.url }}" class="btn btn-ghost" target="_blank"><em>{{ link.text }}</em></a></center></li><br/>
  {% endfor %}
</ul>
<br/>

<h4>Useful Links:</h4>
<ul>
  <li>Software Systems Related:</li>
  <ul>
    {% for resource in site.data.teaching_resources.software %}
      <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
    {% endfor %}
  </ul>
  <br/>
  <li>General:</li>
  <ul>
    {% for resource in site.data.teaching_resources.common %}
      <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
    {% endfor %}
  </ul>
</ul>
<br/>

<h4>Timetable ({{ page.year }}):</h4>
<ul>
  {% for ttable in site.data.software.timetable %}
    <li><em>Group {{ ttable.group }}: {{ ttable.day }} ({{ ttable.time }}) - {{ ttable.location }}</em></li>
  {% endfor %}
</ul>
<br/>

<h4>Contact Info:</h4>
<ul>
  <li>{{ page.contact }}</li>
</ul>

