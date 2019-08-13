---
title: Step Up Masterclasses in the Physical Sciences
coursename: Lego Spectroscopy with a Raspberry Pi
layout: default
year: 2018
permalink: /stepup/

hero: This page relates to the <em>Step Up Masterclasses in the Physical Sciences</em> running at Cardiff University during 2018. Course notes and program files will be available to download here and will be updated as new material is added. Comments and questions welcome at any time.

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Scott Morgan</a> (<a href="mailto:smorgan@bridgend.ac.uk" target="_blank">smorgan@bridgend.ac.uk</a>). Support will be provided via e-mail or during class.
---

<p>{{ page.hero }}</p>
<br/>

<h4>Resources &amp; Useful Links:</h4>
<br/>
<ul>
  {% for lesson in site.data.stepup.lessons %}
    <center><li><a href="{{ lesson.url }}" class="btn btn-ghost"><em>{{ lesson.text }}</em></a></li><br/></center>
  {% endfor %}

  <br/>

  {% for resource in site.data.teaching_resources.stepup %}
    <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Quick Links:</h4>
<ul>
  {% for link in site.data.stepup.links %}
    <li><a href="{{ link.url }}" target="_blank"><em>{{ link.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Timetable:</h4>
<ul>
  {% for ttable in site.data.stepup.timetable %}
    <li><em>{{ ttable.day }} ({{ ttable.time }}) - {{ ttable.location }}</em></li>
  {% endfor %}
</ul>
<br/>

<h4>Contact Info:</h4>
<ul>
  <li>{{ page.contact }}</li>
</ul>
