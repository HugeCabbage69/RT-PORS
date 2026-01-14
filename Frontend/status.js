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
        fillOpacity: 0.9
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
    const rad = rand(150, 400);

    const circle = L.circle([offLat, offLng], {
      radius: rad,
      color: "red",
      fillColor: "red",
      fillOpacity: 0.3
    }).addTo(map);

    calcPriority(offLat, offLng, rad, circle);
  }
}

function calcPriority(lat, lng, radius, circle) {

  const query = `
  [out:json];
  (
    node(around:${radius},${lat},${lng})["amenity"="hospital"];
    node(around:${radius},${lat},${lng})["highway"="traffic_signals"];
    way(around:${radius},${lat},${lng})["landuse"="residential"];
    way(around:${radius},${lat},${lng})["landuse"="commercial"];
  );
  out tags;
  `;

  fetch("https://overpass-api.de/api/interpreter", {
    method: "POST",
    body: query
  })
  .then(r => r.json())
  .then(data => {

    let score = 0;
    let factors = [];

    data.elements.forEach(el => {
      if (el.tags?.amenity === "hospital") {
        score += 7;
        factors.push("+7 Hospital nearby");
      }

      if (el.tags?.highway === "traffic_signals") {
        score += 6;
        factors.push("+6 Traffic signals affected");
      }

      if (el.tags?.landuse === "residential") {
        score += 3;
        factors.push("+3 Residential region");
      }

      if (el.tags?.landuse === "commercial") {
        score += 2;
        factors.push("+2 Commercial region");
      }
    });

    if (score === 0) {
      score = 1;
      factors.push("+1 Individual homes");
    }

    circle.bindPopup(`
      <b>Outage Priority: ${score}</b><br><br>
      ${factors.join("<br>")}
    `);
  })
  .catch(() => {
    circle.bindPopup("Look into it manually");
  });
}

function rand(min, max) {
  return Math.random() * (max - min) + min;
}

// later replace fr() with backend fetch @h3kler
