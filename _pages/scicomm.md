---
title: "Science Engagement"
layout: default
permalink: "/scicomm"
---

<div class="container">
  <h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>

  <div class="row gap-y listrecent listrecent listauthor">
    <div class="col-lg-12 col-md-12 mb-4">
    <div class="p-4 border rounded">
      <h4 class="text-dark mb-0"> Projects </h4><br>
      <div class="p-4 border rounded vdivide">
        {% for projectitem in site.data.outreach.projects %}
          <div class="row vdivide gap-y border rounded">
            <div class="col-md-4 text-center">
              {{ projectitem.title }}
            </div>
            <div class="col-md-4 text-center">
              {{ projectitem.year }}
            </div>
            <div class="col-md-4 text-center">
              {{ projectitem.institution }}
            </div>
           </div>
           <div class="row gap-y border rounded">
            <div class="col-md-12 mb-5">
              {{ projectitem.description }}
              {% if projectitem.partners %}<br><br><strong>Partners:</strong> {{ projectitem.partners }}{% endif %}
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
    <div class="p-4 border rounded">
      <h4 class="text-dark mb-0"> Notable Contributions </h4><br>
      <div class="p-4 border rounded vdivide">
      {% for contributionitem in site.data.outreach.contributions %}
        <div class="row vdivide gap-y border rounded">
          <div class="col-md-4 text-center">
            {{ contributionitem.title }}
          </div>
          <div class="col-md-4 text-center">
            {{ contributionitem.year }}
          </div>
          <div class="col-md-4 text-center">
            {{ contributionitem.institution }}
          </div>
        </div>
      {% endfor %}
      </div>
    </div>
  </div>
</div>
