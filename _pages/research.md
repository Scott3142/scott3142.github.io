---
title: Research
layout: default
permalink: /research/

hero: |

  My current research interests broadly include fluid dynamics, computational modelling and mechanisms for flow transition to turbulence. I have passing interests in all types of computational modelling, in particular relating to mathematical modelling of biological materials and processes.

---

<p>{{ page.hero }}</p>

<p>{{ site.cvlink }}</p>
<br>

<center><h4>Publications</h4></center><br>
<ul>
  {% for pub in site.data.pubs %}
    <li>{{ pub.authors }} <em>{{ pub.title }} {{ pub.journal }} {{ pub.year }}</em></li><br>
  {% endfor %}
</ul>

<br/>

<center><h4>Projects</h4></center><br>
<ul>
  {% for project in site.data.projects %}
    <li>{{ project.title }} | <em>{{ project.institution }} {{ project.year }}</em></li>
  <ul><br/>
    <li>{{ project.description }}</li><br/>
  </ul>
  {% endfor %}
</ul>

<br/>

<center><h4>Notable Contributions</h4></center><br>
<ul>
  {% for contribution in site.data.contributions %}
    {% if contribution.type contains "research" %}
      <li>{{ contribution.title }} | <em>{{ contribution.institution }} {{ contribution.year }}</em></li>
      <ul><br/>
        <li>{{ contribution.description }}</li><br/>
      </ul>
  {% endif %}
  {% endfor %}
</ul>

<br/>

<center><h4>Academic Awards</h4><br>
<ul>
  {% for award in site.data.awards %}
    <li>{{ award.title }} | <em>{{ award.institution }} ({{ award.year }})</em></li><br>
  {% endfor %}
</ul></center>

<br>

<center><h4>Research Funding</h4><br>
<ul>
  {% for fund in site.data.funding %}
    {% if fund.type contains "research" %}
      <li>{{ fund.amount }} {{ fund.duration }} | <em>{{ fund.title }} ({{ fund.year }})</em></li><br/>
    {% endif %}
  {% endfor %}
</ul></center>

<br/>

<center><h4>Conferences &amp; Workshops</h4></center><br>
<ul>
  <li>Organised:</li>
  <ul>
    {% for organisedConference in site.data.conferences.organised %}
      <li>{{ organisedConference.title }} | <em> {{ organisedConference.institution }} ({{ organisedConference.year }})</em> {{ organisedConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Invited Talk:</li>
    <ul>
    {% for talkConference in site.data.conferences.invitedTalk %}
      <li>{{ talkConference.title }} | <em> {{ talkConference.institution }} ({{ talkConference.year }})</em> {{ talkConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Contributed Talk:</li>
    <ul>
    {% for talkConference in site.data.conferences.contributedTalk %}
      <li>{{ talkConference.title }} | <em> {{ talkConference.institution }} ({{ talkConference.year }})</em> {{ talkConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Contributed Poster:</li>
    <ul>
    {% for posterConference in site.data.conferences.contributedPoster %}
      <li>{{ posterConference.title }} | <em> {{ posterConference.institution }} ({{ posterConference.year }})</em> {{ posterConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Attended:</li>
    <ul>
    {% for attendedConference in site.data.conferences.attended %}
      <li>{{ attendedConference.title }} | <em> {{ attendedConference.institution }} ({{ attendedConference.year }})</em> {{ attendedConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
</ul>

<br/>

<center><h4>Society Membership</h4></center><br>
<ul>
  {% for society in site.data.memberships %}
    <li><a href="{{ society.url }}" target="_blank">{{ society.name }}</a></li>
  {% endfor %}
</ul>
