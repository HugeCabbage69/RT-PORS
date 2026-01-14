const map = L.map("map").setView([0, 0], 15);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap contributors"
}).addTo(map);

if ("geolocation" in navigator) {
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const lat = pos.coords.latitude;
      const lng = pos.coords.longitude;

      map.setView([lat, lng], 15);

      L.circleMarker([lat, lng], {
        radius: 6,
        color: "blue",
        fillColor: "blue",
        fillOpacity: 1
      }).addTo(map).bindPopup("You");

      fr(lat, lng);
    },
    () => alert("Location denied")
  );
} else {
  alert("No geo");
}

function fr(lat, lng) {
  for (let i = 0; i < 5; i++) {
    const offLat = lat + rand(-0.01, 0.01);
    const offLng = lng + rand(-0.01, 0.01);

    L.circle([offLat, offLng], {
      radius: rand(150, 400),
      color: "red",
      fillColor: "red",
      fillOpacity: 0.3
    })
    .addTo(map)
    .bindPopup("Power outage report");
  }
}

function rand(min, max) {
  return Math.random() * (max - min) + min;
}

// replace fr() with fetch request @h3kler