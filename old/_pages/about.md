---
title: About
layout: default
permalink: /about_old/

heroEdu: I am currently Digital Lead at Bridgend College, developing bespoke digital content for a variety of curriculum areas. I am passionate about research, technology and education and am interested in new and innovative ways to deliver computing and emerging technologies to students. I am a Raspberry Pi Certified Educator and a Google Level 2 Certified Educator and am always interested in progressing my knowledge and skills. If you would like to find out more, visit my <a href="/teaching">teaching</a> pages or <a href="/contact">get in touch</a>!

heroRes: My PhD in Mathematics at Cardiff University involved research into hydrodynamic stability theory and methods for delaying transition to turbulence in flight. Working alongside my supervisor <a href="https://www.cardiff.ac.uk/people/view/98638-davies-chris" target="_blank">Dr. Chris Davies</a>, I demonstrated that a periodic modulation to the rotation rate of a rotating disk resulted in stabilisation across the boundary layer. To find out more, visit my <a href="/research">research</a> pages or <a href="/contact">get in touch</a>!

---

<p>{{ page.heroEdu }}</p>

<p><br></p>

<p>{{ page.heroRes }}</p>

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

