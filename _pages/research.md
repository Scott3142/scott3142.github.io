---
title: "Research"
layout: default
permalink: "/research"
---

<div class="container">
  <h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>

  <div class="row gap-y listrecent listrecent listauthor">
    <div class="col-lg-12 col-md-12 mb-4">
    <div class="p-4 border rounded">
      <h4 class="text-dark mb-0"> Interests </h4><br>
      <div class="p-4 border rounded vdivide">
        {% for researchitem in site.data.research-interests %}
          <div class="row vdivide gap-y border rounded">
            <div class="col-md-12">
              <ul>
                <li>{{ researchitem.description }}</li>
              </ul>
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
    <div class="p-4 border rounded vdivide">
      <h4 class="text-dark">Publications</h4><br>
      {% for pubsitem in site.data.publications.bc %}
        <div class="row vdivide gap-y border rounded">
          <div class="col-md-12">
          {{ pubsitem.authors }}, {{ pubsitem.title }}| <em>{{ pubsitem.journal }}</em> {% if pubsitem.url %} | <a href="{{ pubsitem.url }}" target="blank">{{ pubsitem.url }}</a>{% endif %}
          </div>
        </div>
      {% endfor %}
      {% for pubsitem in site.data.publications.cu %}
        <div class="row vdivide gap-y border rounded">
          <div class="col-md-12">
          {{ pubsitem.authors }}, {{ pubsitem.title }}| <em>{{ pubsitem.journal }}</em> {% if pubsitem.url %} | <a href="{{ pubsitem.url }}" target="blank">{{ pubsitem.url }}</a>{% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</div>
