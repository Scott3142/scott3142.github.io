---
title: "Contact"
permalink: "/contact"
---

<div class="col-lg-12 mb-4">
	<div class="p-4 border rounded">
		{% for contactlink in site.data.social %}
			<div class="row">
				<p>{{ contactlink.title }} : <a href="{{ contactlink.url }}" target="_blank">{{ contactlink.linkname }}</a></p>
			</div>
		{% endfor %}
	</div>
</div>
