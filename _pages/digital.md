---
title: "Digital at Bridgend College"
layout: default
permalink: "/digital"
---

<div class="container">
  <h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>

  <div class="row gap-y listrecent listrecent listauthor">
    <div class="col-lg-12 col-md-12 mb-4">
      <div class="p-4 border rounded">
        <h4 class="text-dark mb-0"> Title </h4><br>
        <div class="col-md-12 border rounded d-inline-block mt-1 mb-3 pt-2 pb-2 font-weight-normal">
          Subtitle
        </div>
        <div class="p-4 border rounded vdivide">
          <h5 class="text-dark">Sub-subtitle</h5><br>
          {% for item in site.data.itemref %}
            <div class="row vdivide gap-y border rounded">
              <div class="col-md-12">
               {{ some.liquid.syntax }}
              </div>
            </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>
