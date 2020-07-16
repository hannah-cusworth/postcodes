import folium

map = folium.Map(
	location=[55.3781,-3.4360],
	zoom_start=6,
)

map.save('templates/postcode_site/map.html')

