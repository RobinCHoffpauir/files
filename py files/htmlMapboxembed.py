# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 02:42:19 2021

@author: Robin
"""
#embed into html <head> tag

<script src='https://api.mapbox.com/mapbox-gl-js/v2.3.1/mapbox-gl.js'></script>
<link href='https://api.mapbox.com/mapbox-gl-js/v2.3.1/mapbox-gl.css' rel='stylesheet' />

#add to <body> tag
<div id='map' style='width: 400px; height: 300px;'></div>
<script>
mapboxgl.accessToken = 'pk.eyJ1IjoicGFybGF5a2luZyIsImEiOiJja3RzZGs0eHQxZjh0MzFycmNxbndxZWM1In0.SthEWzkgYZKXtuXaSwoJtg';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11'
});
</script>