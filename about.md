---
title: About
layout: default
permalink: /about/

heroRes: I am currently a PhD student studying Mathematics at Cardiff University, working alongside my supervisor <a href="https://www.cardiff.ac.uk/people/view/98638-davies-chris" target="_blank">Dr. Chris Davies</a>. My research is based primarily in fluid dynamics and in particular hydrodynamic stability theory. I am interested in laminar flow control techniques and have looked at oscillatory flows over rotating disks and flat plates. To find out more, visit my <a href="/research">research</a> pages or <a href="/contact">get in touch</a>!

heroEdu: I am also interested in computing for education, and have run several workshops and classes using Raspberry Pi computers, BBC MicroBit and Arduinos. I am a Raspberry Pi Certified Educator and am very interested in new and innovative ways to deliver computing to school students. If you would like to find out more, visit my <a href="/teaching">teaching</a> pages or <a href="/contact">get in touch</a>!
---

<p>{{ page.heroRes }}</p>

<p><br></p>

<p>{{ page.heroEdu }}</p>

<p><br></p>

<p>{{ site.cvlink }}</p>

<br/>

<h4>Collaborators &amp; Partners</h4>
<br/>
<ul>
  {% for partner in site.data.partners %}
    <li style="{{ partner.style }}"><a href="{{ partner.url }}" target="_blank"><img src="{{ partner.image }}"/></a></li>
  {% endfor %}
</ul>

