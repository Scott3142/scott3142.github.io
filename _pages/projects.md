---
title: "Projects"
layout: default
permalink: "/projects"
---

<div class="container">
<h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>
  <div class="row gap-y listrecent listrecent listauthor">
    {% for projectlink in site.data.projects %}
      <div class="col-lg-6 col-md-6 mb-4">
        <div class="p-4 border rounded">
          <div class="row">
            <div class="col-md-3 mb-4 mb-md-0"><img alt="{{ projectlink.title }}" src="{{ projectlink.image }}" class="rounded-circle" height="80" width="80"></div>
            <div class="col-md-9">
              <a href="{{ projectlink.url }}">
                <h4 class="text-dark mb-0"> {{ projectlink.title }} </h4>
                <div class="excerpt">{{ projectlink.description }}</div>
              </a>
            </div>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
